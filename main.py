import os
import json

estoque = {}
file = input("Digite o nome do arquivo:\n> ") + ".json"

############################################################
#                        Funções
############################################################

def rotina():
    try:
        with open(file, 'r', encoding="utf-8") as arquivo:
            estoque = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não existe, deseja criar?".center(50))
        print("(s/n)".center(50))
        ans = input("> ")
        if ans == "s":
            with open(file, 'w') as arquivo:
                json.dump(estoque, arquivo)

def carregar_arquivo(estoque, file):
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
                json.dump(estoque, arquivo)
                return print("Arquivo criado com sucesso".center(50))
        else:
            print("\n\33[31mOpção inválida.\33[0m")
            carregar_arquivo(estoque, file)
    else:
        with open(file, 'w', encoding="utf-8") as arquivo:
            json.dump(estoque, arquivo)
            return print("Arquivo criado com sucesso".center(50))

def adicionar_produto(estoque, file):
    if os.path.exists(f"{file}"):
        print("\nEscolha uma opção:")
        print("1 - Adicionar Produto")
        print("2 - Adicionar Quantidade")
        menu_estoque = input("\n> ")
        if menu_estoque == "1":
            try:
                nome = input("\nDigite o nome do produto:\n> ").lower()
                quantidade = int(input("\nDigite a quantidade disponível:\n> "))
                estoque[nome] = quantidade
                with open(file, 'w') as arquivo:
                    json.dump(estoque, arquivo, indent=4)
                    print("\n\33[32mArquivo atualizado com sucesso.\33[0m\n")
            except Exception as e:
                print(e)

        elif menu_estoque == "2":
            try:
                for i, g in estoque.items():
                    print(f"Item: {i} || Quant: {g}")
                nome = input("\nDigite o nome do produto:\n> ").lower()
                if nome in estoque:
                    quantidade = int(input("\nDigite a quantidade para adicionar:\n> "))
                    estoque[nome] += quantidade
                    with open(file, 'w') as arquivo:
                        json.dump(estoque, arquivo, indent=4)
                        print("\n\33[32mArquivo atualizado com sucesso.\33[0m\n")
                else:
                    print("\n\33[31mProduto precisa estar no estoque\33[0m\n")
            except Exception as e:
                print(e)
        
        else:
            print("\n\33[31mOpção inválida.\33[0m")
            adicionar_produto(estoque, file)

def remover_produto(estoque, file):
    if os.path.exists(f"{file}"):
        print("\nEscolha uma opção:")
        print("1 - Remover Produto")
        print("2 - Remover Quantidade")
        menu_estoque = input("\n> ")
        if menu_estoque == "1":
            try:
                nome = input("\nDigite o nome do produto:\n> ").lower()
                del estoque[nome]
                with open(file, 'w') as arquivo:
                    json.dump(estoque, arquivo, indent=4)
                    print("\n\33[32mArquivo atualizado com sucesso.\33[0m\n")
            except Exception as e:
                print(e)

        elif menu_estoque == "2":
            try:
                for i, g in estoque.items():
                    print(f"Item: {i} || Quant: {g}")
                nome = input("\nDigite o nome do produto:\n> ").lower()
                if nome in estoque:
                    quantidade = int(input("\nDigite a quantidade para remover:\n> "))
                    estoque[nome] -= quantidade
                    with open(file, 'w') as arquivo:
                        json.dump(estoque, arquivo, indent=4)
                        print("\n\33[32mArquivo atualizado com sucesso.\33[0m\n")
                else:
                    print("\n\33[31mProduto precisa estar no estoque\33[0m\n")
            except Exception as e:
                print(e)
        
        else:
            print("\n\33[31mOpção inválida.\33[0m")
            adicionar_produto(estoque, file)



############################################################
#                         Código
############################################################

rotina()

while True:
    print("Escolha uma opção".center(50, "="))
    print("1 - Escolher arquivo".center(50))
    print("2 - Entradas".center(50))
    print("3 - Saidas".center(50))
    print("4 - Visualizar estoque".center(50))
    menu = input("\n> ")
    
    if menu == "1":
        carregar_arquivo(estoque, file)
    elif menu == "2":
        adicionar_produto(estoque, file)
    elif menu == "3":
        remover_produto(estoque, file)
        
        