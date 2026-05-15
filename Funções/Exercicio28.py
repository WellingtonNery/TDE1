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

help(media)