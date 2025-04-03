import sys
from pathlib import Path

with open("DEBUG_EXECUTION_OK.txt", "w") as f:
    f.write("✅ O SCRIPT ESTÁ SENDO EXECUTADO!\n")

print("===== DEBUG DE CAMINHO E IMPORTAÇÃO =====")

current_file = Path(__file__).resolve()
print(f"📍 Este arquivo está em: {current_file}")

project_root = current_file.parents[1]
src_path = project_root / "src"
ferris_core_path = src_path / "ferris_core"

print(f"📁 Existe src? {src_path.exists()}")
print(f"📁 Existe ferris_core? {ferris_core_path.exists()}")

print("\n🧠 sys.path:")
for p in sys.path:
    print(" -", p)

print("\n🚀 Tentando importar ferris_core.sequential_thinking...")
try:
    sys.path.insert(0, str(src_path))
    from ferris_core import sequential_thinking
    print("✅ Importação funcionou!")
except Exception as e:
    print("❌ Falha ao importar ferris_core:", e)

print("===== FIM DO DEBUG =====")
