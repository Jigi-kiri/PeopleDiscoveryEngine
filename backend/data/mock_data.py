import json
import os

def load_mock_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'mock_data.json')
    
    with open(json_path, 'r') as f:
        return json.load(f)

mock_data = load_mock_data()