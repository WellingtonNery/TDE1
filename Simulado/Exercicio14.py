num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo!")
    if num % 2 == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")
else:
    print("O número é negativo!")