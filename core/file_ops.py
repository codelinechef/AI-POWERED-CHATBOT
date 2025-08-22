import os

def create_file(name, content = ""):
    with open(name, 'w') as f:
        f.write(content)

def read_file(name):
    with open(name, "r") as f:
        return f.read()