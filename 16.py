
numeros = []

tam = int(input("Digite o tamanho da Lista: "))


print("Digite os números da lista: ")
for i in range(tam):
    num = int(input(f"{i + 1}º:"))
    numeros.append(num)
        
soma = 0
    
for i in numeros:
    soma += i

print("\nSoma: ",soma)
