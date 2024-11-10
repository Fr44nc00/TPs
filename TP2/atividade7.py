# Lista definida
listaDefinida = [10, 20, 30, 40, 50, 60, 70, 80]

def inverterLista(lista):
    """
    Inverte a ordem dos elementos em uma lista e retorna a
    lista invertida.
    
    Parâmetros:
        lista (list): A lista que será invertida.
        
    Retorna:
        lista: A mesma lista, agora invertida.
    """
    # Invertendo a ordem dos elementos na lista original
    # O método reverse() altera a lista original
    lista.reverse()  
    
    # Retornando a lista invertida
    return lista  

# Chamando a função para inverter a lista e exibe o resultado
print(inverterLista(listaDefinida))