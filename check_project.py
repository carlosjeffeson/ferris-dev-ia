import os
import sys

def print_header(msg):
    print(f"\n🔍 {msg}\n{'-' * (len(msg) + 4)}")

def check_init_files(root):
    print_header("Verificando arquivos __init__.py 📦")
    missing = False
    for dirpath, dirnames, filenames in os.walk(root):
        if "__pycache__" in dirpath:
            continue
        if any(f.endswith(".py") for f in filenames) and "__init__.py" not in filenames:
            print(f"❌ Faltando: {os.path.relpath(dirpath, root)}/__init__.py")
            missing = True
    if not missing:
        print("✅ Todos os pacotes possuem __init__.py")

def check_sys_path():
    print_header("Verificando sys.path 🐍")
    src_path = os.path.abspath("src")
    if src_path in sys.path:
        print(f"✅ src está no sys.path -> {src_path}")
    else:
        print(f"❌ src NÃO está no sys.path -> {src_path}")

def print_tree(root, prefix=""):
    files = os.listdir(root)
    files.sort()
    for i, name in enumerate(files):
        path = os.path.join(root, name)
        connector = "├── " if i < len(files) - 1 else "└── "
        if os.path.isdir(path):
            print(f"{prefix}{connector}📁 {name}")
            print_tree(path, prefix + ("│   " if i < len(files) - 1 else "    "))
        elif name.startswith("test_") and name.endswith(".py"):
            print(f"{prefix}{connector}🧪 {name}")
        else:
            print(f"{prefix}{connector}📄 {name}")

def check_project():
    print_header("📂 Árvore de Diretórios (src)")
    print_tree("src")

    check_init_files("src")
    check_sys_path()

    print("\n✅ Verificação concluída. Agora rode o pytest novamente.")

if __name__ == "__main__":
    check_project()
