from typing import Dict, List, Any, Optional, Set, Tuple
import numpy as np
import pandas as pd
from dataclasses import dataclass, field
import structlog

logger = structlog.get_logger(__name__)

@dataclass
class GraphNode:
    node_id: str
    node_type: str  # "customer", "card", "ip", "device", "merchant"
    attributes: Dict[str, Any] = field(default_factory=dict)
    degree: int = 0
    in_degree: int = 0
    out_degree: int = 0
    risk_prior: float = 0.0

@dataclass
class GraphEdge:
    source_id: str
    target_id: str
    edge_type: str
    timestamp: float
    weight: float = 1.0
    amount: float = 0.0

class FinancialTransactionGraph:
    """In-memory bipartite and heterogeneous graph network for fraud propagation."""
    
    def __init__(self, decay_halflife_hours: float = 72.0):
        self.nodes: Dict[str, GraphNode] = {}
        self.adjacency: Dict[str, List[Tuple[str, float, float]]] = {}  # node -> [(neighbor, weight, timestamp)]
        self.decay_factor = np.log(2) / (decay_halflife_hours * 3600.0)
        self._fraud_seeds: Set[str] = set()

    def add_node(self, node_id: str, node_type: str, risk_prior: float = 0.0, **attrs) -> GraphNode:
        if node_id not in self.nodes:
            self.nodes[node_id] = GraphNode(
                node_id=node_id,
                node_type=node_type,
                risk_prior=risk_prior,
                attributes=attrs
            )
            self.adjacency[node_id] = []
        return self.nodes[node_id]

    def add_edge(self, source_id: str, target_id: str, edge_type: str, timestamp: float, amount: float = 0.0, weight: float = 1.0):
        self.add_node(source_id, "unknown")
        self.add_node(target_id, "unknown")
        
        self.adjacency[source_id].append((target_id, weight, timestamp))
        self.adjacency[target_id].append((source_id, weight, timestamp))
        
        self.nodes[source_id].degree += 1
        self.nodes[target_id].degree += 1

    def mark_fraud_seed(self, node_id: str):
        if node_id in self.nodes:
            self._fraud_seeds.add(node_id)
            self.nodes[node_id].risk_prior = 1.0

    def compute_personalized_pagerank(self, source_node: str, alpha: float = 0.85, max_iter: int = 50, tol: float = 1e-6) -> Dict[str, float]:
        if source_node not in self.nodes:
            return {}
        
        nodes_list = list(self.nodes.keys())
        N = len(nodes_list)
        if N == 0:
            return {}
        
        node_to_idx = {nid: i for i, nid in enumerate(nodes_list)}
        idx_to_node = {i: nid for i, nid in enumerate(nodes_list)}
        
        # Power iteration
        p = np.zeros(N, dtype=np.float64)
        p[node_to_idx[source_node]] = 1.0
        
        r = np.ones(N, dtype=np.float64) / N
        teleport = np.zeros(N, dtype=np.float64)
        teleport[node_to_idx[source_node]] = 1.0
        
        for iteration in range(max_iter):
            r_next = np.zeros(N, dtype=np.float64)
            for u_idx, u_id in idx_to_node.items():
                nbrs = self.adjacency.get(u_id, [])
                deg = len(nbrs)
                if deg > 0:
                    flow = (alpha * r[u_idx]) / deg
                    for v_id, _, _ in nbrs:
                        if v_id in node_to_idx:
                            r_next[node_to_idx[v_id]] += flow
                else:
                    r_next += (alpha * r[u_idx]) / N
            
            r_next += (1.0 - alpha) * teleport
            err = np.sum(np.abs(r_next - r))
            r = r_next
            if err < tol:
                break
                
        return {idx_to_node[i]: float(r[i]) for i in range(N)}

    def calculate_ego_network_fraud_density(self, node_id: str, depth: int = 2, current_time: Optional[float] = None) -> Dict[str, float]:
        if node_id not in self.nodes:
            return {
                "ego_size": 0,
                "ego_fraud_seed_count": 0,
                "ego_fraud_ratio": 0.0,
                "ego_weighted_fraud_score": 0.0
            }
        
        visited: Set[str] = {node_id}
        queue: List[Tuple[str, int, float]] = [(node_id, 0, 1.0)]  # (curr, dist, weight_path)
        
        fraud_seeds_found = 0
        total_nodes = 0
        weighted_score = 0.0
        
        while queue:
            curr_id, dist, path_wt = queue.pop(0)
            total_nodes += 1
            
            if curr_id in self._fraud_seeds and curr_id != node_id:
                fraud_seeds_found += 1
                weighted_score += path_wt * (1.0 / (dist + 1))
            
            if dist < depth:
                for nbr_id, edge_wt, edge_ts in self.adjacency.get(curr_id, []):
                    if nbr_id not in visited:
                        visited.add(nbr_id)
                        time_decay = 1.0
                        if current_time is not None:
                            dt = max(0.0, current_time - edge_ts)
                            time_decay = np.exp(-self.decay_factor * dt)
                        queue.append((nbr_id, dist + 1, path_wt * edge_wt * time_decay))
                        
        ratio = (fraud_seeds_found / max(1, total_nodes - 1)) if total_nodes > 1 else 0.0
        return {
            "ego_size": total_nodes,
            "ego_fraud_seed_count": fraud_seeds_found,
            "ego_fraud_ratio": float(ratio),
            "ego_weighted_fraud_score": float(weighted_score)
        }
