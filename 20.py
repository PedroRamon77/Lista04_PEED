def maiorNota(alunos):
    maior_nota = float("-inf")
    nomeAlunoMaiorNota = ""

    for aluno in alunos:
        nome = aluno["nome"]
        nota = aluno["nota"]

        if nota > maior_nota:
            maior_nota = nota
            nomeAlunoMaiorNota = nome

    return nomeAlunoMaiorNota 

numAlunos = int(input("Digite o número de alunos: "))

alunos = []

for i in range(numAlunos):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    aluno = {"nome": nome, "nota": nota}
    alunos.append(aluno)

alunoMaiorNota = maiorNota(alunos)

print("\nAluno com maior nota: ", alunoMaiorNota)


