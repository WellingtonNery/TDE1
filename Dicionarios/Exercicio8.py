notas = {"Wellington":10, "João":2, "Lucas":5}
alterado = input("Digite o nome do aluno para buscar a nota (Wellington, João, Lucas): ")
nota = notas.get(alterado)
if nota:
    print(f"Nota: {nota}")
else:
    print("Aluno inexistente!")