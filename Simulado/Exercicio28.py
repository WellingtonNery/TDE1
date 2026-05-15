num = int(input("Digite um número para saber o seu fatorial: "))
fat = 1

for i in range (num, 0, -1):
    fat *= i

print(f"O fatorial deste número é: {fat}")