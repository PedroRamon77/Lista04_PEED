def comparar(lista1, lista2):
    set_lista1 = set(lista1)
    set_lista2 = set(lista2)
    comum = set_lista1.intersection(set_lista2)
    return list(comum)

tam = int(input("Digite o tamanho das listas: "))

lista1 = []
lista2 = []

print("Digite os números da lista 01:")
for i in range(tam):
    num = int(input(f"{i + 1}:"))
    lista1.append(num)

print("Digite os números da lista 02:")
for i in range(tam):
    num = int(input(f"{i + 1}:"))
    lista2.append(num)   

resultado = comparar(lista1, lista2)

print("Elementos comuns:", resultado)
