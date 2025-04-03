"""
Agent Base - Ferris DEV IA Ultimate - PRO
-----------------------------------------
Responsável por inicializar o agente principal (Ferris),
integrando Sequential Thinking, Think Tool Server e Desktop Commander.
"""

# -------------------
# Imports Necessários
# -------------------
import os
import sys
from dotenv import load_dotenv
from pathlib import Path
from autogen import AssistantAgent, UserProxyAgent

# -------------------
# Ajuste do sys.path para reconhecer /src como raiz dos módulos
# -------------------
base_dir = Path(__file__).resolve().parents[1]
src_dir = base_dir / "src"
sys.path.append(str(src_dir))

# -------------------
# Imports Internos do Projeto
# -------------------
from ferris_core.sequential_thinking import create_sequential_group
from ferris_core import think_tool_server

# -------------------
# Carregamento do Ambiente (.env)
# -------------------
env_path = base_dir.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(f"❌ API Key não carregada! Verifique se o .env está em {env_path}")
print("✅ API KEY carregada com sucesso.")

# -------------------
# Configuração do LLM
# -------------------
llm_config = {
    "api_key": OPENAI_API_KEY,
    "model": "gpt-4-turbo"
}

# -------------------
# Criação do Grupo Inteligente (Planner + Executor)
# -------------------
usuario, manager = create_sequential_group(llm_config)

# -------------------
# Função Principal do Ferris
# -------------------
def ferris_execute(task: str) -> str:
    """
    Ferris pensa, planeja e executa comandos reais via Desktop Commander.

    Parâmetros:
    ----------
    task : str
        Comando ou tarefa em linguagem natural.

    Retorno:
    -------
    str
        Plano e resultado da execução.
    """
    subtasks = think_tool_server.analyze_task(task)
    plan = think_tool_server.format_plan(subtasks)
    result = think_tool_server.execute(task)
    return f"📋 Plano Gerado:\n{plan}\n\n💻 Resultado da Execução:\n{result}"

# -------------------
# Execução Direta (Teste)
# -------------------
if __name__ == "__main__":
    print(ferris_execute("echo Hello Ferris!"))
