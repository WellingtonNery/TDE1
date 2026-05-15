nomes = input("Digite os nomes separados por vírgula: ")

lista_nomes = nomes.split(",")

dicionario = dict.fromkeys(lista_nomes, 0)

print(dicionario)