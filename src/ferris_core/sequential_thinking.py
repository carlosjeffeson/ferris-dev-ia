"""
Sequential Thinking - Ferris DEV IA
-----------------------------------
Este módulo implementa o raciocínio estruturado do Ferris,
baseado em Planner + Executor + Usuário (UserProxy).
O objetivo é sempre decompor problemas e executar com qualidade.
"""

from autogen import GroupChat, GroupChatManager, AssistantAgent, UserProxyAgent

def create_sequential_group(llm_config: dict):
    """
    Cria um grupo sequencial de agentes:
    - Planner: Responsável por planejar passos
    - Executor: Responsável por executar tarefas planejadas
    - Usuario: Interface interativa

    :param llm_config: Configuração do modelo LLM
    :return: Tuple (usuario, manager)
    """

    # --- Agente Planner ---
    planner = AssistantAgent(
        name="Planner",
        llm_config=llm_config,
        system_message=(
            "Você é um engenheiro de software altamente experiente. "
            "Sua missão é decompor qualquer problema proposto em passos sequenciais claros, lógicos "
            "e otimizados para eficiência e qualidade de código. Considere sempre boas práticas."
        )
    )

    # --- Agente Executor ---
    executor = AssistantAgent(
        name="Executor",
        llm_config=llm_config,
        system_message=(
            "Você é um programador sênior responsável por implementar as tarefas planejadas pelo Planner. "
            "Seu foco é gerar código limpo, funcional, bem estruturado e fácil de manter."
        )
    )

    # --- Agente Usuario ---
    usuario = UserProxyAgent(
        name="Usuario",
        code_execution_config=False
    )

    # --- Configuração do Chat em Grupo ---
    group_chat = GroupChat(
        agents=[planner, executor, usuario],
        messages=[],
        max_round=20  # Limite de interações por sessão
    )

    # --- Gerenciador do Grupo ---
    manager = GroupChatManager(
        groupchat=group_chat,
        llm_config=llm_config
    )

    return usuario, manager
