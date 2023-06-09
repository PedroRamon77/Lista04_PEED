from fila import Fila

fila = Fila()

print("Digite: ")
while True:
    numero = int(input())
    if numero < 0:
        break
    fila.enqueue(numero)

print("\nElementos da fila que foram removidos: ")
while not fila.is_empty():
    elemento = fila.dequeue()
    print(elemento)
