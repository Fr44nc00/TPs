# Faça um programa que calcule o Índice de Massa Corporal (IMC)
# do usuário e forneça feedback com base no valor (por exemplo,
# abaixo do peso, peso normal, sobrepeso).

def calcularIMC(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        print("Você está abaixo do peso ideal!")
    elif imc >= 18.5 and imc <= 24.9:
        print("Você está na faixa de peso ideal.")
    else:
        print("Você está acima do peso ideal!")
        
peso = float(input("Informe seu peso (em kg): "))
altura = float(input("Informe sua altura (em m): "))

calcularIMC(peso, altura)