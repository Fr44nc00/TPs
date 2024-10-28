# Crie um programa que pergunte a idade do usuário e verifique
# se ele é maior de idade ou não.

def calculoFaixaEtaria(idade):
    if idade >= 18:
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade!")
        
idade = int(input("Informe sua idade: "))
calculoFaixaEtaria(idade)