lista = [8, 3, 1, 7, 0, 10, 2]

sublistas = [[x] for x in lista]

while len(sublistas) > 1:
    novas = []

    for i in range(0, len(sublistas), 2):
        if i + 1 < len(sublistas):
            esq = sublistas[i]
            dir = sublistas[i + 1]

            resultado = []
            a = b = 0

            while a < len(esq) and b < len(dir):
                if esq[a] <= dir[b]:
                    resultado.append(esq[a])
                    a += 1
                else:
                    resultado.append(dir[b])
                    b += 1

            resultado.extend(esq[a:])
            resultado.extend(dir[b:])

            novas.append(resultado)
        else:
            novas.append(sublistas[i])

    sublistas = novas

print(sublistas[0])