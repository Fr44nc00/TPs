def paresImpares(aLista):
    '''
    Função que separa os elementos de uma lista em pares
    e ímpares.
    
    Parâmetros:
    aLista (list): Lista que será separada.
    '''
    
    # Listas para armazenar os elementos separados
    pares = []
    impares = []
    
    # Iterando sobre os números da lista
    for n in aLista:
        # Verificando se o número é par (divisível por 2)
        if (n % 2 == 0):
            # Adiciona o número à lista de pares
            pares.append(n)
        else:
            # Adiciona o número à lista de ímpares
            impares.append(n)
    
    # Informando ao usuário os números separados
    print(f"Os números pares da lista são: {pares}")
    print(f"Os números ímpares da lista são: {impares}")

def separandoLista():
    '''
    Função para informar a lista e enviá-la para a
    separação entre pares e ímpares.
    '''
    
    # Definindo a lista de números
    lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
    print(f"Lista: {lista}")
    
    # Chamando a função para separar a lista
    paresImpares(lista)
    
# Chamando a função para separar os números da lista
separandoLista()