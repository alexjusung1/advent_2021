from os import path

def get_text(file_name) -> str:
    with open(path.join(path.dirname(__file__), file_name), 'r') as f:
        return f.read()