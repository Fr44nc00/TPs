# Importando a biblioteca "math"
import math

def verificarPrimos(n):
    """
    Verifica se o número informado é primo.

    Um número é primo se for maior que 1 e não for divisível
    por nenhum número além de 1 e ele mesmo.

    Parâmetros:
        num (int): O número a ser verificado.

    Retorna:
        boolean: True se o número for primo, False caso
        contrário.
    """
    # Números menores ou iguais a 1 não são primos
    if n <= 1:
        return False 
    
    # Verificando se o número é divisível por algum número
    # entre 2 e a raiz quadrada do número
    for i in range(2, int(math.sqrt(n)) + 1):  
        # Se o número for divisível por algum i, não é primo
        if n % i == 0:
            return False 
    
    # Se não for divisível por nenhum número, é primo
    return True  

def informarIntervalo():
    """
    Solicita ao usuário um intervalo inferior e superior e
    encontra os números primos dentro desse intervalo.

    Exibe a quantidade de números primos encontrados e quais
    são.
    """
    # Solicitando o início e o fim do intervalo ao usuário
    comeco = int(input("Informe o começo do intervalo: "))
    fim = int(input("Informe o fim do intervalo: "))

    # Contador para os números primos encontrados
    contador = 0  
    
    # Lista para armazenar os números primos encontrados
    primos = []  
    
    # Iterando sobre todos os números no intervalo
    for i in range(comeco, fim + 1):  
        # Verificando se o número é primo
        if verificarPrimos(i):  
            # Adicionando o número à lista de primos
            primos.append(i)  
            # Incrementando o contador de números
            # primos encontrados
            contador += 1  

    # Exibindo a quantidade e a lista de números
    # primos encontrados
    print(f"\nQuantidade de primos encontrados: {contador}")
    print(f"Os números primos encontrados foram: {primos}")

# Chamando a função para executar o programa
informarIntervalo()