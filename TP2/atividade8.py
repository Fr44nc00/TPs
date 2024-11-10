# Definindo as duas listas de números
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [10, 20, 30, 40, 50, 60, 70, 80]

def somaListas(lista1, lista2):
    """
    Soma os elementos correspondentes de duas listas e
    retorna uma nova lista com os resultados.

    Parâmetros:
    lista1 (list): Primeira lista de números a ser somada.
    lista2 (list): Segunda lista de números a ser somada.

    Retorna:
    lista3 (list): Uma nova lista com a soma dos elementos
    correspondentes das duas listas.
    """

    # Lista onde o resultado da soma será armazenado
    lista3 = []
    
    # Iterando sobre os índices das listas para somar os
    # elementos correspondentes
    for i in range(len(lista1)):
        soma = lista1[i] + lista2[i]  # Somando os elementos
        # correspondentes
        lista3.append(soma)  # Adicionando o resultado na
        # lista3
    
    # Retornando a lista com as somas
    return lista3  

# Chamando a função e imprimindo o resultado
print(somaListas(lista1, lista2))