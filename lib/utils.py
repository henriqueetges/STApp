import json
import tomllib

def open_contents(file) -> dict:
    try:
        with open(file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading file:{e}")
        return {}

def load_toml(file)-> dict:
    try:
        with open(file, 'rb') as f:
            return tomllib.load(f)
    except ImportError as e:
        print(f"Error loading toml{e}")
        
