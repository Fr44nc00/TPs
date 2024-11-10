def maiorMenorNumeros(aLista):
    '''
    Função que define quais são o maior e menor números
    em uma lista.
    
    Parâmetros:
    aLista (list): Lista de números
    '''
    
    # Inicializando as variáveis do maior e menor números.
    # O valor de maior é 0, e o valor de menor é 200,
    # assumindo que todos os números na lista serão
    # maiores que 0 e menores que 200.
    maior = 0
    menor = 200
    
    # Iterando sobre os elementos da lista
    for n in aLista:
        # Caso o número seja maior que o maior número atual,
        # substitui o maior número
        if (n > maior):
            maior = n
        # Caso o número seja menor que o menor número atual,
        # substitui o menor número
        elif (n < menor):
            menor = n
    
    # Informando ao usuário quais são o maior e menor números
    print(f"O maior número na lista é {maior}.")
    print(f"O menor número na lista é {menor}.")
    
def somaMediaNumeros(aLista):
    '''
    Função que define qual a soma dos elementos e a média de
    uma lista de números.
    
    Parâmetros:
    aLista (list): Lista de números
    '''
    
    # Somando todos os elementos na lista
    total = 0
    for i in aLista:
        total += i
        
    # Calculando a média dos elementos na lista
    media = total / len(aLista)
    
    # Informando os resultados da soma e da média ao usuário
    print(f"A soma de todos os elementos na lista é {total}.")
    print(f"A média dos números na lista é {media}.")

def estatisticasLista():
    '''
    Função que estabelece a lista e chama funções que irão
    calculá-las e exibí-las.
    '''
    # Definindo a lista de números
    lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
    print(f"Lista: {lista}")
    
    # Chamando as funções para calcular o maior, menor,
    # soma e média
    maiorMenorNumeros(lista)
    somaMediaNumeros(lista)
    
# Chamando a função para executar as estatísticas da lista
estatisticasLista()