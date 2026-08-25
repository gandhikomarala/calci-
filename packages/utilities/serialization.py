"""Custom JSON encoders and serializers for ML models and NumPy types."""

import json
import datetime
import numpy as np

class MLJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

def serialize_json(data: any) -> str:
    return json.dumps(data, cls=MLJSONEncoder)

def deserialize_json(json_str: str) -> any:
    return json.loads(json_str)
