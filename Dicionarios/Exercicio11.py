dic = {"Joao": "17", "Lucas": "18", "Wellington": "19"}
print(f"Dicionario atual: {dic}")

while True:
    print("[1] Consultar dados dos usuários")
    print("[2] Buscar usuário pelo nome")
    print("[3] Adicionar um novo usuário")
    print("[4] Atualizar idade de um usuário existente")
    print("[5] Remover um usuário")
    print("[6] Remover o último elemento no dicionário")
    print("[7] Criar cópia do dicionário")
    print("[8] Inicializar um novo dicionário")
    print("[9] Atualizar o dicionário atual a partir de outro dicionário")
    print("[10] Limpar todos os dados do sistema")
    print("[11] Crir um novo dicionário a partir de uma lista de tuplas")
    print("[12] Sair")
    opcaoMenu = int(input("Digite a opção desejada:"))

    if opcaoMenu == 1:
        print("[1] Mostrar o nome dos usuários")
        print("[2] Mostrar a idade dos usuários")
        print("[3] Mostrar os pares nome-idade")

        opcao = int(input("Digite a opção desejada:"))

        if opcao == 1:
            for nome in dic.keys():
                print(nome)

        elif opcao == 2:
            for idade in dic.values():
                print(idade)

        elif opcao == 3:
            for nome, idade in dic.items():
                print(nome, idade)
        else:
            print("Opção inválida!")
        print()

    elif opcaoMenu == 2:
        escolha2 = input("Digite pelo nome que deseja buscar: ")
        buscado = dic.get(escolha2)
        if buscado:
            print(buscado)
        else:
            print("Usuário inexistente!")
        print()


    elif opcaoMenu == 3:
        usuarioAdicionar = input("Digite o nome do usuário: ")
        idadeAdicionar = int(input("Digite a idade do usuário: "))
        dic[usuarioAdicionar] = idadeAdicionar
        print(dic)
        print()

    elif opcaoMenu == 4:
        usuarioAtualizar = input("Digite o nome do usuário para atualizar a idade: ")
        idadeAtualizar = int(input("Digite a idade: "))
        dic[usuarioAtualizar] = idadeAtualizar
        print(dic)
        print()

    elif opcaoMenu == 5:
        usuarioRemover = input("Digite o usuário a ser removido: ")
        dic.pop(usuarioRemover)
        print(dic)
        print()

    elif opcaoMenu == 6:
        dic.popitem()
        print(dic)
        print()

    elif opcaoMenu == 7:
        dic2 = dic.copy()
        usuarioAtu = input("Digite o nome do usuário para atualizar a idade: ")
        idadeAtu = int(input("Digite a idade: "))
        dic2[usuarioAtu] = idadeAtu
        print(dic)
        print(dic2)
        print()

    elif opcaoMenu == 8:
        iddPadrao = int(input("Qual será a idade padrao dos usuários? "))
        nomesUsuários = input("Digite o nome dos usuários separados por uma virgula: ").split(",")
        dicNovo = dict.fromkeys(nomesUsuários, iddPadrao)
        print(dicNovo)
        print()

    elif opcaoMenu == 9:
        nomesUpd = input("Digite o nome dos usuários separados por uma vírgula: ").split(",")
        idadesUpd = tuple(input("Digite a idade dos usuários separados por uma vírgula: ").split(","))
        dicUpd = dict(zip(nomesUpd, idadesUpd))
        dic.update(dicUpd)
        print(dic)
        print()

    elif opcaoMenu == 10:
        confirmacao = input("Tem certeza que deseja limpar todos os dados? ")
        if confirmacao == "sim" or "Sim":
            dic.clear()
            print(dic)
        else:
            print(dic)
        print()

    elif opcaoMenu == 11:
        nomes2 = input("Digite o nome dos usuários separados por uma vírgula: ").split(",")
        idades2 = tuple(input("Digite a idade dos usuários separados por uma vírgula: ").split(","))
        listaTuplas = list(zip(nomes2, idades2))
        dic2 = dict(listaTuplas)
        print(f"Dicionário antigo: {dic}")
        print(f"Novo dicionário: {dic2}")
        print()