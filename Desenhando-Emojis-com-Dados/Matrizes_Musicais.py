biblioteca_musical = {

  "Toques": [

    {"Alegre": ([440, 480], [520, 560])},

    {"Triste": ([200, 150], [100, 50])}

  ]

}



# Transposição de uma matriz 2×2:

# original → transposta

# [a, b]    [a, c]

# [c, d]    [b, d]

#

# Regra geral: transposta[i][j] = original[j][i]



# NÍVEL 1 — percorre a lista de toques

for toque in biblioteca_musical["Toques"]:



  # NÍVEL 2 — percorre cada par nome/matriz dentro do dicionário do toque

  for nome, matriz in toque.items():

    linhas = len(matriz)

    colunas = len(matriz[0])



    # Cria a grade transposta usando compreensão de lista

    transposta = [[0] * linhas for _ in range(colunas)]



    # NÍVEL 3 — preenche a transposta percorrendo índice a índice

    for i in range(linhas):

      for j in range(colunas):

        transposta[j][i] = matriz[i][j] # inverte i↔j



    # .update() substitui o valor da chave no dicionário existente

    toque.update({nome: transposta})



# Resultado esperado:

# Alegre: [[440, 520], [480, 560]]

# Triste: [[200, 100], [150, 50]]

for toque in biblioteca_musical["Toques"]:

  for nome, matriz in toque.items():

    print(f"{nome}:", matriz)

