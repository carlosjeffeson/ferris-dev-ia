# --- Script para listar estrutura de pastas e arquivos do seu projeto ---

import os

def listar_estrutura(diretorio, prefixo=""):
    for item in os.listdir(diretorio):
        caminho = os.path.join(diretorio, item)
        if os.path.isdir(caminho):
            print(f"{prefixo}📂 {item}/")
            listar_estrutura(caminho, prefixo + "    ")
        else:
            print(f"{prefixo}📄 {item}")

if __name__ == "__main__":
    print("📌 Estrutura de Arquivos do Projeto:\n")
    raiz = os.getcwd()  # Vai pegar a pasta atual como raiz
    listar_estrutura(raiz)
