def sistema_notas_turma():

  total_alunos = int(input("Quantos alunos existem na turma? "))



  for i in range(1, total_alunos + 1):

    aluno_nome = input("Nome do aluno: ")

    nota1 = float(input("Nota 1: "))

    nota2 = float(input("Nota 2: "))



    media_aluno = (nota1 + nota2) / 2



    if media_aluno >= 7.0:

      print(f"{aluno_nome}: Aprovado com média {media_aluno}")

    elif media_aluno >= 5.0:

      print(f"{aluno_nome}: Recuperação (Média: {media_aluno})")

    else:

      print(f"{aluno_nome}: Reprovado")



sistema_notas_turma()