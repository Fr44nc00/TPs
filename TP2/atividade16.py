def informarNome():
    '''
    Recebe o nome de um aluno
    
    Retorno:
    oNome (str): Nome do aluno informado
    '''
    oNome = input("\nInforme o nome do aluno: ")
    return oNome

def calcularMediaAluno(oAluno):
    '''
    Calcula a média de um aluno com base em suas notas
    
    Parâmetros:
    oAluno (list): Lista contendo o nome e as notas do aluno
    '''
    # Calcula e exibe a média do aluno com uma casa decimal
    media = (oAluno[1] + oAluno[2]) / 2
    print(f"Média: {round(media, 1)}")
    
    # Exibe se o aluno está aprovado ou em prova final
    if media >= 6:
        print(f"O(A) aluno(a) {oAluno[0]} está aprovado.")
    else:
        print(f"O(A) aluno(a) {oAluno[0]} está em prova final.")

def calcularMediaTurma(notas, aTurma):
    '''
    Calcula a média total da turma
    
    Parâmetros:
    notas (float): Soma das notas de todos os alunos
    aTurma (list): Lista contendo os dados dos alunos
    '''
    # Calcula e exibe a média da turma com uma casa decimal
    media = notas / len(aTurma)
    print(f"A média das notas da turma é: {round(media, 1)}")

def inserirNotas():
    # Armazena a soma das notas e os dados de todos os alunos
    turmaNotas = 0
    turma = []
    
    FIM = "fim"
    nome = informarNome()
    
    # Recebe nome e notas dos alunos até o nome ser "fim"
    while nome.lower() != FIM:
        nota1 = float(input("Informe a primeira nota: "))
        nota2 = float(input("Informe a segunda nota: "))
        # Soma as notas de cada aluno
        turmaNotas += nota1 + nota2
        
        # Adiciona o aluno com suas notas à lista da turma
        aluno = [nome, nota1, nota2]
        turma.append(aluno)
        
        # Calcula e exibe a média do aluno
        calcularMediaAluno(aluno)
        
        # Solicita o nome do próximo aluno
        nome = informarNome()
        
    # Calcula e exibe a média da turma
    calcularMediaTurma(turmaNotas, turma)
    
# Inicia o programa
inserirNotas()