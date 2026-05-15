contador = 0

while True:
    num = float(input("Digite um número (negativo para encerrar): "))

    if num < 0:
        print(f"Foram digitados {contador} números pares!")
        break

    if num % 2 == 0:
        contador += 1