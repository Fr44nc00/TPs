# Faça um programa que converta um número fornecido de minutos em horas
# e minutos, e depois faça o inverso, convertendo horas e minutos de
# volta para minutos totais.

def converter_horas():
    min = int(input("Informe a quantidade de minutos: "))
    
    div = min // 60
    resto = min % 60
    
    if resto == 0:
        print(f"Convertido para {div} horas.")
    elif div == 0:
        print(f"Convertido para {resto} minutos.")
    else:
        print(f"Convertido para {div} horas e {resto} minutos.")
    
    converter = int(input("Gostaria de converter o valor de volta para minutos?\n1- Sim // 2- Não\n"))
    if converter == 1:
        converter_minutos(div, resto)
    
def converter_minutos(h, m):
    totalMin = (h * 60) + m
    
    print(f"Convertido para {totalMin} minutos.")

def conversao():
    opcoes = int(input("Qual conversão gostaria de fazer?\n1- Converter minutos pra horas e minutos // 2- Converter horas e minutos para minutos\n"))

    match(opcoes):
        case 1:
            converter_horas()
        case 2:
            horas = int(input("Informe primeiro a quantidade de horas: "))
            min = int(input("Agora informe a quantidade de minutos: "))
            converter_minutos(horas, min)
    
conversao()