contador = 0
soma = 0

while True:
    num = float(input("Digite um número (0 para encerrar): "))

    soma += num

    if num == 0:
        print(f"Soma dos números digitados: {soma}")
        break