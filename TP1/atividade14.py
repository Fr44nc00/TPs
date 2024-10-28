# Escreva um programa que permita ao usuário votar em
# três opções diferentes e, no final, exiba o número
# de votos de cada opção.

chocolate = 0
morango = 0
baunilha = 0

while True:
    voto = int(input("\nInforme o voto:\n1 para chocolate, 2 para morango, 3 para baunilha\nVoto: "))
    
    match(voto):
        case 1:
            chocolate += 1
        case 2:
            morango += 1
        case 3:
            baunilha += 1
    
    opcao = int(input("\nDeseja informar outro voto?\n1- Sim // 2- Não\n"))
    
    if opcao == 2:
        print(f"\nOs votos para cada sabor foram:\nChocolate: {chocolate} // Morango: {morango} // Baunilha: {baunilha}")
        break