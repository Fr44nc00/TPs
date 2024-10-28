# Crie um programa que peça ao usuário seu nome e sobrenome usando
# input e, em seguida, combine-os para formar uma
# saudação personalizada.

nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")

nomeCompleto = f"{nome} {sobrenome}"

saudacao = f"Seja bem vindo(a), {nomeCompleto}!"
print(saudacao)