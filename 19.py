def maiorPalavra(palavras):
    maior_palavra = ""

    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

    return maior_palavra

palavras = []
palavras = input("Digite as palavras: ").split()

maior = maiorPalavra(palavras)

print("\nMaior Palavra: ",maior)