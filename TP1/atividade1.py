# Crie um programa que peça ao usuário para inserir dois números e,
# em seguida, calcule e exiba a soma, subtração, multiplicação,
# divisão e divisão inteira desses números.

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

soma = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2

print(f"\n--Operações com os números--\nSoma dos números: {soma}\nSubtração dos números: {sub}\nMultiplicação dos números: {multi}\nDivisão dos números: {div}")