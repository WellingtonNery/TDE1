dicionario = {"Nome 1": "João", "Nome 2": "Lucas", "Nome 3": "Wellington"}

chRemov = input("Digite uma chave para remover (Nome 1, Nome 2, Nome 3): ")

dicionario.pop(chRemov)

dicionario.popitem()

qtdDados = int(input("Digite a quantidade de dados para entrar no dicionário: "))

for i in range(qtdDados):
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    dicionario.update({chave: valor})

print(dicionario)
