from smithery import load_client

# Carrega o client do Smithery
code_mcp = load_client("code_mcp")

def list_files():
    return code_mcp.list_files()

def read_file(path):
    return code_mcp.read_file(path=path)

def write_file(path, content):
    return code_mcp.write_file(path=path, content=content)

def execute_command(command):
    return code_mcp.execute(command=command)