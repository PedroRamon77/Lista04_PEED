from fila import Fila

def verifica_palindromo(frase):
    fila = Fila()

    for char in frase:
        fila.enqueue(char)

    fila_inversa = Fila()
    for char in reversed(frase):
        fila_inversa.enqueue(char)

    while not fila.is_empty() and not fila_inversa.is_empty():
        if fila.dequeue() != fila_inversa.dequeue():
            return False
    return fila.is_empty() and fila_inversa.is_empty()

frase = input("Digite uma frase:")

if verifica_palindromo(frase):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")


