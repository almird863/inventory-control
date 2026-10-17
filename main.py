import os
import json
from functions import *

estoque = {}
file = input("Digite o nome do arquivo:\n> ") + ".json"

with open(file, 'r', encoding="utf-8") as arquivo:
    estoque = json.load(arquivo)

while True:
    print("Escolha uma opção".center(50, "="))
    print("1 - Escolher arquivo".center(50))
    print("2 - Adicionar produto".center(50))
    print("3 - Adicionar quantidade".center(50))
    print("4 - Remover produto".center(50))
    print("5 - Remover quantidade".center(50))
    menu = input("\n> ")
    
    if menu == "1":
        carregar_arquivo(estoque, file)