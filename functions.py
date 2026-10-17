import os
import json

def carregar_arquivo(var):
    file = input("Digite o nome do arquivo:\n> ") + ".json"
    if os.path.exists(f"{file}"):
        print("ATENÇÃO: Arquivo já existe".center(50, "="))
        print("Editar mesmo assim?".center(50))
        print("(s/n)".center(50))
        answer = input("\n> ").lower().strip()
        if answer == "s":
            with open(file, 'r', encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return dados
        elif answer == "n":
            file = input("Digite o nome do novo arquivo:\n> ") + ".json"
            with open(file, 'w', encoding="utf-8") as arquivo:
                json.dump(var, arquivo)
                return print("Arquivo criado com sucesso".center(50))
    else:
        with open(file, 'w', encoding="utf-8") as arquivo:
            json.dump(var, arquivo)
            return print("Arquivo criado com sucesso".center(50))

def adicionar_produto()