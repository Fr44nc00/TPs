# Desenvolva um programa que verifique se uma
# palavra ou frase inserida pelo usuário é um
# palíndromo (lê-se igual de trás para frente).

def detectarPalindromo(palavra):
    palavraMinuscula = palavra.lower()
    palavraInvertida = palavraMinuscula[::-1]
    
    if palavraMinuscula == palavraInvertida:
        print(f'A palavra "{palavra}" é um palíndromo.')
    else:
        print(f'A palavra "{palavra}" não é um palíndromo.')

palavra = input("Digite uma palavra: ")
detectarPalindromo(palavra)
