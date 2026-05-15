def calculadora(num1, num2, operacao):
    """
    Retorna uma operação

    Parâmetros:
        num1 (int/float): primeiro número
        num2 (int/float): segundo número
        operador (char): operador do cálculo

    Retorno:
        int/float: resultado da operação
    """
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    elif operacao == "^":
        return num1 ** num2

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operador = input("Digite o operador: ")

print(f"Resultado: {calculadora(numero1, numero2, operador)}")