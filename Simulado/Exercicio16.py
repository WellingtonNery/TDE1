vetor = []

for i in range(2):
    num = float(input("Digite um número:"))
    vetor.append(num)

if vetor[0] > vetor[1]:
    print("O primeiro número é maior!")
else:
    print("O segundo número é maior!")