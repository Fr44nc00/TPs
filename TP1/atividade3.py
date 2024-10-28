# Escreva um programa que receba dois nomes de usuário e os combine
# de maneira criativa para formar um novo nome.

nome1 = input("Insira o primeiro nome: ")
nome2 = input("Insira o segundo nome: ")

metade1 = len(nome1) // 2
metade2 = len(nome2) // 2

novoNome = nome2[:metade2] + nome1[metade1:]

print(f"O novo nome é {novoNome}.")