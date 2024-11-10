def exibindoLista(aLista):
    '''
    Função que exibe a lista
    
    Parâmetros:
    aLista (list): Lista a ser exibida
    '''
    # Exibe a lista de números
    print(f"A lista de números é:\n{aLista}")

def exibindoListaInvertida(aLista):
    '''
    Função que exibe a lista invertida
    
    Parâmetros:
    aLista (list): Lista a ser invertida
    '''
    
    # Inverte a lista recebida
    aLista.reverse()
    
    # Exibe a lista invertida
    print(f"\nA lista de números invertida é:\n{aLista}")

def criandoLista():
    # Criando a variável da lista
    lista = []
    
    # Loop que só para quando o número inserido for 0
    numero = 1
    while numero != 0:
        # Solicitando que o usuário insira um número
        numero = int(input("\nInsira um número: "))
        
        # Inserindo o número informado na lista
        lista.append(numero)
    
    # Chamando as funções de exibir e inverter a lista
    exibindoLista(lista)
    exibindoListaInvertida(lista)

# Informando ao usuário as regras da definição da sequência
print("Informe números para a sequência. Caso deseje parar, insira '0'.")
# Chamando a função para iniciar o processo
criandoLista()