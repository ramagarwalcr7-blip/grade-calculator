import json
import os
from constants import DATA_FILE

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"subjects": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)