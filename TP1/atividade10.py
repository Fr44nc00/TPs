# Escreva um programa que combine elementos aleatórios de
# listas diferentes (personagens, ações, locais) para
# criar uma história curiosa.

import random

nomes = ["Pedro", "Mateus", "Marcos", "Lucas", "Manoel"]
nome = random.choice(nomes)
acoes = ["pescar", "lavar roupa", "tomar café da manhã", "tomar banho", "ler um livro"]
acao = random.choice(acoes)
lugares = ["Teyvat", "Kanto", "Alabasta", "Brasar", "Tandor"]
lugar = random.choice(lugares)
pets = ["cachorro", "gato", "porco", "piriquito", "papagaio"]
pet = random.choice(pets)
nomesPets =["Ben", "Andy", "Bidu", "Floquinho", "Fred"]
nomePet = random.choice(nomesPets)

print(f"{nome}, após acordar na terra de {lugar}, foi {acao} acompanhado de seu {pet} de estimação, chamado {nomePet}.")