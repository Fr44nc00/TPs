# Definindo a lista utilizada no código
lista = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]

def buscandoNumero(n):
    '''
    Função que busca um número informado na lista.
    
    Parâmetros:
    n (int): Número informado
    
    Retorno:
    Valor do condicional (1 se encontrado, -1 caso contrário)
    '''
    
    # Condicional que retorna 1 se o número estiver na lista
    # ou -1 caso contrário
    if n in lista:
        return 1
    else:
        return -1

def informandoNumero():
    '''
    Função que pede ao usuário para informar um número e
    diz se ele está ou não presente na lista, bem como sua
    posição.
    '''
    
    # Solicitando ao usuário para inserir o número a ser
    # buscado
    numero = int(input("Informe o número a ser buscado: "))
    
    # Chamando a função de buscar o número na lista
    achou = buscandoNumero(numero)
    
    # Caso o número seja encontrado, informa ao usuário sua
    # posição
    if achou > 0:
        print(f"O número foi encontrado na lista no index {lista.index(numero)}")
    else:
        print("O número não se encontra na lista.")
        
# Chamando a função para buscar o número informado
informandoNumero()