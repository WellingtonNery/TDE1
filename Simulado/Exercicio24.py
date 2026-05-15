contador = 0
num = 0

while True:
   entrada = input("Digite um número (não digite nada para encerrar):")
   if entrada == "":
       break

   num = int(entrada)

   if num < 0:
       contador += 1

print(f"Foram digitados {contador} números negativos!")