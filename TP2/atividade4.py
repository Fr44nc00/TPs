def tabuada():
    """
    Exibe a tabuada dos números de 1 a 10.
    """
    
    # Loop para cada número de 1 a 10
    for numero in range(1, 11):
        
        # Exibe o título da tabuada do número
        print(f"\n\nTabuada do {numero}:")
        
        # Loop para multiplicar o número de 1 a 10
        for multiplicador in range(1, 11):
            
            # Calcula o resultado da multiplicação
            resultado = numero * multiplicador
            
            # Exibe o resultado da multiplicação
            print(f"{numero} x {multiplicador} = {resultado}")
            
# Chamando a função para exibir as tabuadas
tabuada()