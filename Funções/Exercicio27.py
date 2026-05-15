def media(lista):
    """
    Retorna a média de uma lista.

    Parâmetros: lista (list/array): uma lista de inteiros/float

    Retorno: int/float: média de uma lista
    """

    soma = 0

    for i in lista:
        soma += i

    return soma/len(lista)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(media(lista))