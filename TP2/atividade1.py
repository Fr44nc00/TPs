def contando_vogais():
    """
    Lê uma sequência de caracteres até um ponto final ('.')
    e conta o número de vogais.
    
    Exibe o total de vogais ao final.
    """
    vogais = 0
    caractere = ""
    
    # Lê cada caractere até que seja um ponto ('.')
    while caractere != ".":
        caractere = input("Entre com um caractere: ").lower()
        print(f"Caractere inserido = {caractere}")
        
        # Incrementa o contador se o caractere for uma vogal
        if caractere in "aeiou":
            vogais += 1
    
    # Exibe o total de vogais
    print(f"Número de vogais inseridas: {vogais}")

# Executa a função
contando_vogais()