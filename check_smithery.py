# check_smithery_pro.py

import sys
import os

print("🔄 Verificando Smithery...\n")

try:
    from smithery import load_client
    print("✅ smithery importado")
except ImportError:
    print("❌ smithery NÃO encontrado (pip install smithery?)")
    sys.exit(1)

try:
    code_mcp = load_client("code_mcp")
    print("✅ code_mcp carregado")
except Exception as e:
    print(f"❌ Falha ao carregar code_mcp: {e}")
    sys.exit(1)

# Checando se o cliente tem as funções esperadas
required_funcs = ["list_files", "read_file", "write_file", "execute"]

missing = []

for func in required_funcs:
    if not hasattr(code_mcp, func):
        missing.append(func)
        print(f"❌ Falta: {func}")
    else:
        print(f"✅ Encontrado: {func}")

if not missing:
    print("\n🚀 Tudo OK! Pode rodar seus testes agora.")
else:
    print("\n⚠️ MCP carregou mas faltam funções importantes!")
