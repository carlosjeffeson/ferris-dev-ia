"""
Test Think Tool Server
----------------------
Este script testa o funcionamento do think_tool_server isoladamente.
"""

import sys
from pathlib import Path

# Adiciona o diretório 'src' ao sys.path para que o package ferris_core seja encontrado
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ferris_core.think_tool_server import analyze_task, format_plan

# Exemplo de tarefa para testar
tarefa = "Preciso de ajuda para desenvolver um sistema de cadastro de clientes."

# Analisa a tarefa
subtasks = analyze_task(tarefa)

# Exibe as subtarefas formatadas
print("Subtarefas sugeridas:")
print(format_plan(subtasks))