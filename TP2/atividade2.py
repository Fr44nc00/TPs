def somaMedia():
    """
    Calcula e exibe a soma e a média dos números de 1 a 100.
    """
    total = 0
    
    # Calcula a soma dos números de 1 a 100
    for numero in range(1, 101):
        total += numero
    
    # Calcula a média
    media = total / 100
    
    # Exibe os resultados
    print(f"A soma de todos os números entre 1 e 100 é {total}.")
    print(f"A média de todos os números entre 1 e 100 é {media}.")

# Executa a função
somaMedia()
