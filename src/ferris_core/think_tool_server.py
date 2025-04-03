"""
Think Tool Server - Ferris DEV IA
---------------------------------
Este módulo fornece ao Planner ferramentas de raciocínio
para decompor e organizar tarefas de forma estruturada.
"""

from typing import List

def analyze_task(task: str) -> List[str]:
    """
    Analisa uma tarefa em linguagem natural e sugere subtarefas sequenciais.

    Parâmetros:
    ----------
    task : str
        Descrição geral da tarefa em linguagem natural.

    Retorno:
    -------
    List[str]
        Lista de subtarefas geradas.
    """
    # Pré-processamento simples
    task = task.lower().strip()

    # Decomposição baseada em palavras-chave
    if "cadastro" in task and "cliente" in task:
        subtasks = [
            "Definir requisitos do sistema",
            "Modelar o banco de dados de clientes",
            "Criar formulários de cadastro e edição",
            "Implementar CRUD de clientes",
            "Configurar rotas e views",
            "Testar sistema",
            "Documentar"
        ]
    else:
        subtasks = [
            "Analisar requisitos do sistema",
            "Projetar arquitetura",
            "Desenvolver backend",
            "Desenvolver frontend",
            "Integrar componentes",
            "Testar",
            "Documentar"
        ]
    return subtasks

def format_plan(subtasks: List[str]) -> str:
    """
    Formata a lista de subtarefas em um plano textual numerado.

    Parâmetros:
    ----------
    subtasks : List[str]
        Lista de subtarefas.

    Retorno:
    -------
    str
        Texto formatado com numeração.
    """
    return "\n".join([f"{i+1}. {sub}" for i, sub in enumerate(subtasks)])

__all__ = ["analyze_task", "format_plan"]
