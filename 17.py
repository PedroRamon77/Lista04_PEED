def strings(lista):
    novaLista = []
    for string in lista:
        if len(string) > 5:
            novaLista.append(string)
    return novaLista

nomes = []
nomes = input("Digite as strings: ").split()

strings6 = strings(nomes)

print("\strings com mais de 5 caracteres:")
for nome in strings6:
    print(nome)



