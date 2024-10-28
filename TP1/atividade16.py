# Neste exercício, você deverá escrever um programa em
# Python que verifique se um número fornecido pelo
# usuário é par ou ímpar. Imprima uma mensagem indicando
# se o número é par ou ímpar.

num = int(input("Informe o número: "))

if num % 2 == 0:
    print("Este número é par.")
else:
    print("Este número é ímpar.")