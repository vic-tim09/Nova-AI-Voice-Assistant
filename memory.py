import json

MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def set_memory(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

def get_memory(key):
    memory = load_memory()
    return memory.get(key)