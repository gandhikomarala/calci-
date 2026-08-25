import pytest
from ml.features.financial_graph_network_features import FinancialTransactionGraph

def test_graph_node_and_edge_addition():
    g = FinancialTransactionGraph()
    g.add_node("cust_1", "customer", risk_prior=0.1)
    g.add_node("card_1", "card", risk_prior=0.0)
    g.add_edge("cust_1", "card_1", "used_card", timestamp=1000.0, amount=250.0)
    
    assert "cust_1" in g.nodes
    assert "card_1" in g.nodes
    assert g.nodes["cust_1"].degree == 1
    assert g.nodes["card_1"].degree == 1

def test_graph_pagerank():
    g = FinancialTransactionGraph()
    g.add_node("c1", "customer")
    g.add_node("c2", "customer")
    g.add_edge("c1", "c2", "transfer", timestamp=1000.0)
    
    pr = g.compute_personalized_pagerank("c1")
    assert len(pr) == 2
    assert pr["c1"] > 0
    assert pr["c2"] > 0

def test_ego_fraud_density():
    g = FinancialTransactionGraph()
    g.add_node("victim", "customer")
    g.add_node("fraudster", "customer")
    g.add_node("mule", "customer")
    g.add_edge("victim", "mule", "transfer", timestamp=1000.0)
    g.add_edge("mule", "fraudster", "transfer", timestamp=1050.0)
    g.mark_fraud_seed("fraudster")
    
    density = g.calculate_ego_network_fraud_density("victim", depth=2, current_time=2000.0)
    assert density["ego_size"] == 3
    assert density["ego_fraud_seed_count"] == 1
    assert density["ego_fraud_ratio"] == 0.5
