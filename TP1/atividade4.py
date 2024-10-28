def operacao():
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    opr = input("Informe a operação (+, -, * ou /): ")

    match opr:
        case "+":
            soma = num1 + num2
            msg = f"A soma dos números é {soma}."
        case "-":
            sub = num1 - num2
            msg = f"A subtração dos números é {sub}."
        case "*":
            multi = num1 * num2
            msg = f"A multiplicação dos números é {multi}."
        case "/":
            if num2 == 0:
                print("Não é possível dividir por zero!")
                operacao()
            else:
                div = num1 / num2
                msg = f"A divisão dos números é {div}."
        case _:
            print("Operador inválido! Tente novamente.")
            operacao()
    
    print(msg)
    
operacao()