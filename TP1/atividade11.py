# Faça um programa que simule o lançamento de um dado. O
# usuário deve escolher quantos dados jogar e o programa
# deve exibir os resultados.

import random
dados = []

def rolarDado():
    dado = random.randint(1, 6)
    dados.append(dado)

def adicionarDados():
    while True:
        if dados == []:
            resposta1 = int(input("Deseja rolar um dado?\n1- Sim // 2- Não\n"))

            match (resposta1):
                case 1:
                    rolarDado()
                case 2:
                    break
        else:
            resposta2 = int(input("Deseja rolar mais um dado?\n1- Sim // 2- Não\n"))

            match (resposta2):
                case 1:
                    rolarDado()
                case 2:
                    break
                
    if dados:
        print("Segue(m) o(s) resultado(s) do(s) dado(s):")
        for dado in dados:
            print(dado)
            
adicionarDados()