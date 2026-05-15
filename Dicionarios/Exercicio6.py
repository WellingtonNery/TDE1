dic1 = {"Nome":"Lucas", "Cor favorita": "Azul", "Sexo":"Masculino"}
dic2 = dict(dic1)

alterado = input("Digite uma chave pra ser alterada (Nome, Cor favorita, Sexo): ")
valorNovo = input("Digite o valor a ser alterado: ")

dic2[alterado] = valorNovo

print(dic1)
print(dic2)