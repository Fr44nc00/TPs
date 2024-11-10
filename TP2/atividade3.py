def calcularFatorial(n):
    """
    Calcula o fatorial de um número inteiro positivo.

    Parâmetros:
        n (int): Número para o qual o fatorial será calculado.

    Retorna:
        int: O fatorial de 'n'. Retorna 1 se 'n' for 0 ou 1.
    """
    if n == 0 or n == 1:
        # Fatorial de 0 ou 1 é 1
        return 1
    
    resultado = 1
    # Calcula o fatorial multiplicando de 2 até n
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def inserirNumeros():
    """
    Lê uma sequência de números inteiros positivos e exibe
    o fatorial de cada número inserido, terminando quando o usuário
    digitar zero.
    """
    numeros = []
    # Garante que o loop seja executado
    numero = 1
    
    while numero != 0:
        numero = int(input("Informe um número inteiro positivo para a sequência: "))
        
        # Validação de número positivo
        if numero < 0:
            print("Informe apenas números positivos!")
        elif numero > 0:
            # Adiciona o número à lista
            numeros.append(numero)
            
    # Exibe o fatorial de cada número
    for i in numeros:
        fatorial = calcularFatorial(i)
        print(f"O fatorial de {i} é {fatorial}.")

# Executa a função
inserirNumeros()