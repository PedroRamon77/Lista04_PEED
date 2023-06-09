from fila import Fila

fila = Fila()

while True:
    print("\nMenu: ")
    print("1. Adicionar número na fila")
    print("2. Remover número da fila")
    print("3. Tamanho da fila")
    print("4. Mostrar fila")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = int(input("Digite o número a ser adicionado: "))
        fila.enqueue(numero)
        print("Número adicionado à fila\n")

    elif opcao == "2":
        try:
            numero_removido = fila.dequeue()
            print("Número removido da fila: ", numero_removido)
            print("\n")
        except IndexError:
            print("A fila está vazia\n")

    elif opcao == "3":
        tamanho = fila.size
        print("Tamanho da fila: ", tamanho)
        print("\n")

    elif opcao == "4":
        if fila.is_empty():
            print("A fila está vazia\n")
        else:
            print("Fila:")
            current_item = fila.head
            while current_item is not None:
                print(current_item.value)
                current_item = current_item.next

    elif opcao == "5":
        print("\n\nPrograma Encerrado")
        break

    else:
        print("Opção Ínválida\nTente Novamente")

