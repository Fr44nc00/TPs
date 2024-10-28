# Crie um programa que classifique as palavras inseridas
# pelo usuário como curtas (menos de 5 letras) ou longas
# (5 letras ou mais).

def palavraTamanho():
    palavra= str(input("\nInforme a palavra: "))
    
    if len(palavra) < 5:
        print("Palavra curta.")
    else:
        print("Palavra longa.")
    
    while True:
        opcao = int(input("\nDeseja informar outra palavra?\n1- Sim // 2- Não\n"))
        
        if opcao == 1:
            palavraTamanho()
        else:
            break
        
def informarPalavra():
    while True:
        opcao = int(input("Deseja informar uma palavra?\n1- Sim // 2- Não\n"))
        
        if opcao == 1:
            palavraTamanho()
        else:
            break
        
informarPalavra()