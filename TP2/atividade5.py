def progressao():
    """
    Recebe dois números inteiros e gera uma sequência de 50
    termos em Progressão Aritmética (PA), com base na
    diferença entre o segundo e o primeiro termo.
    """
    
    # Solicitando os dois primeiros termos da progressão
    termo1 = int(input("Informe o primeiro termo: "))
    termo2 = int(input("Informe o segundo termo: "))
    
    # Calculando a constante da progressão (diferença
    # entre os dois primeiros termos)
    const = termo2 - termo1
    
    # Criando a lista da progressão e adicionando os dois
    # primeiros termos
    progArit = [termo1, termo2]
    
    # Calculando os próximos termos da progressão
    contagem = 2  # Já temos 2 termos, então restam 48
    while contagem < 50:
        
        # Calculando o próximo termo
        termo3 = termo2 + const
        
        # Atualizando o termo2 para o próximo cálculo
        termo2 = termo3
        
        # Adicionando o termo à lista
        progArit.append(termo2)
        
        # Incrementando a contagem
        contagem += 1
    
    # Exibindo os 50 primeiros termos da progressão aritmética
    print("Os 50 primeiros termos da progressão aritmética são: ")
    print(progArit)
        
# Chamando a função para gerar a PA
progressao()