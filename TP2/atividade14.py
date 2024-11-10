def validacao():
    '''
    Função que valida a entrada de um número
    '''
    # Define o valor inicial para que o loop ocorra
    numero = -1
    
    # Loop que continua enquanto o número não for válido
    while numero < 0:
        try:
            numero = int(input("Informe um número para a validação: "))
            if numero < 0:
                print("\nNúmero inválido! Tente novamente.\n")
        except ValueError:
            print("\nEntrada inválida! Por favor, insira um número inteiro.\n")
    
    print("\nNúmero válido.")
            
# Chamando a função
validacao()  