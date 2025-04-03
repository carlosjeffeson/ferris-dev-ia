from autogen import AssistantAgent, UserProxyAgent
import os
from dotenv import load_dotenv
from pathlib import Path
import sys

# --- IMPORTANTE ---
# Adiciona o /src ao sys.path explicitamente
sys.path.append(str(Path(__file__).resolve().parents[1]))

# Agora sim podemos importar normalmente
from ferris_core.sequential_thinking import create_sequential_group

# Configuração do ambiente
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=str(env_path), encoding="utf-8", override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(f"API Key não carregada! Verifique se o .env está em {env_path}")

print("API KEY carregada:", OPENAI_API_KEY)

# Configuração do modelo
llm_config = {
    "api_key": OPENAI_API_KEY,
    "model": "gpt-4-turbo"
}

# Criação do grupo inteligente (Planner + Executor + Usuario)
usuario, manager = create_sequential_group(llm_config)

# Início da conversa com o Planner e Executor
usuario.initiate_chat(manager, message="Preciso de ajuda para desenvolver um sistema de cadastro de clientes.")