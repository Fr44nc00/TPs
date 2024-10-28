# Escreva um programa onde o usuário deve adivinhar um número
# secreto. O programa deve dizer se o palpite está correto,
# muito alto ou muito baixo.

import random

def adivinhe():
    num = random.randint(1, 20)
    while True:
        palpite = int(input("Tente adivinhar o número secreto: "))

        if palpite == num:
            print("Acertou!!")
            break
        elif abs(num - palpite) <= 3:
            print("Errou por pouco! Tente novamente.")
        elif palpite < num:
            print("Muito baixo! Tente um número maior.")
        else:
            print("Muito alto! Tente um número menor.")

adivinhe()
