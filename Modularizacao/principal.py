import operacoes as op
import usuario as us

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

print(f"Soma = {op.soma(num1, num2)}")
print(f"Subtração = {op.subtracao(num1, num2)}")
print(f"Multiplicação = {op.multiplicacao(num1, num2)}")
print(f"Divisao = {op.divisao(num1, num2)}")

nome = input("Digite seu nome: ")

us.cadastro(nome)
us.mensagem()