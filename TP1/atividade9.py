# Desenvolva um programa que aplique descontos progressivos
# com base no valor da compra: desconto de 10% para compras
# acima de R$100, 15% para compras acima de R$200, seguindo
# a projeção até R$500, para valores maiores do que esse, o
# desconto é fixado em 25%.

def calcularDesconto(valor):
    if valor > 400.0:
        valor = valor - (valor * 0.25)
    elif valor > 300.0:
        valor = valor - (valor * 0.2)
    elif valor > 200.0:
        valor = valor - (valor * 0.15)
    elif valor > 100.0:
        valor = valor - (valor * 0.1)
    print(f"O valor a ser pago é R${valor}.")

valor = int(input("Informe o valor total da compra: "))

calcularDesconto(valor)