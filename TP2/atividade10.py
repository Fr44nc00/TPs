def filtragemNumeros(aLista, aMedia):
    '''
    Recebe uma lista e uma média, passando os elementos da
    lista que forem maior que a média para uma outra lista.
    
    Parâmetros:
    aLista (list): Lista recebida
    aMedia (float): Média dos números na lista
    '''
    
    # Definindo a lista onde os números filtrados serão
    # armazenados
    lista = []
    
    # Achando os números maiores que a média
    for n in aLista:
        if (n >= aMedia):
            # Inserindo os números maiores que a média
            # na nova lista
            lista.append(n)
    
    # Mostrando ao usuário os números filtrados
    print(f"Os números maiores que a média dos números inseridos foram:\n{lista}")

def calcularMedia(oTotal, aLista):
    '''
    Recebe uma lista e uma soma dos números, calcula a média e
    chama a função de filtragem para exibir os números maiores
    que a média.
    
    Parâmetros:
    oTotal (int): Soma dos números da lista
    aLista (list): Lista recebida
    '''
    
    # Calculando a média dos números na lista
    media = oTotal / len(aLista)
    print(f"\nMédia dos números inseridos: {media}")
    
    # Passando a lista e a média para a função de filtragem
    filtragemNumeros(aLista, media)

def formandoSequencia():
    '''
    Recebe números de uma sequência e os armazena em uma
    lista até que o número inserido seja 0.
    '''
    
    # Definindo as variáveis da lista e o total de números
    numeros = []
    total = 0
    
    # Loop que só para quando o número inserido for 0
    numero = 1
    while numero != 0:
        numero = int(input("\nInsira um número: "))
        # Inserindo o número informado na lista
        numeros.append(numero)
        # Somando o número informado ao total
        total += numero
        
    # Passando a soma dos números e a lista deles para
    # calcular a média
    calcularMedia(total, numeros)

# Informando ao usuário as regras da definição da sequência
print("Informe números para a sequência. Caso deseje parar, insira '0'.")
# Chamando a função para iniciar o processo
formandoSequencia()