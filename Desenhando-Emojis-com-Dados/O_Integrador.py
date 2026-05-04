# ── Desafio 3: Cardápio de Lanchonete ────────────────────────────────────────

# Contexto: uma lanchonete guarda seu cardápio como um dicionário.

# Cada categoria (ex: "Lanches") contém uma lista de pratos.

# Cada prato é uma tupla imutável: (nome, preço, calorias).

#

# Estruturas usadas:

# dicionário → o cardápio inteiro, com categorias como chaves

# lista   → os pratos dentro de cada categoria (dá pra adicionar/remover)

# tupla   → dados fixos de cada prato (não queremos alterar preço por acidente)

#

# Métodos obrigatórios:

# .pop()  → remove o último prato da lista

# .insert() → recoloca ele em outra posição

# .keys() → itera pelas categorias do cardápio



cardapio = {

  "Lanches": [

    ("X-Burguer", 18.90, 520),

    ("X-Bacon",  22.50, 680),

    ("Veggie Wrap", 16.00, 390),

  ],

  "Bebidas": [

    ("Suco de Laranja", 8.00, 110),

    ("Refrigerante", 6.50, 150),

    ("Água com Gás", 5.00, 0),

  ],

  "Sobremesas": [

    ("Pudim",    9.00, 280),

    ("Sorvete 2 bolas", 12.00, 340),

  ]

}



# ── .pop() — o garçom retirou o último item de Lanches do balcão

prato_retirado = cardapio["Lanches"].pop()

print(f"Prato retirado temporariamente: {prato_retirado[0]}")



# ── .insert() — ele volta, mas agora como destaque (posição 0)

cardapio["Lanches"].insert(0, prato_retirado)

print(f"Destaque do dia: {cardapio['Lanches'][0][0]}\n")



# ── 3 níveis de FOR para imprimir o cardápio completo ────────────

total_itens = 0

menor_caloria = ("?", 9999, 9999) # vamos achar o prato mais leve



# FOR 1 — percorre as categorias do dicionário pelo nome da chave

for categoria in cardapio.keys():

  print(f"{'─'*40}")

  print(f" {categoria.upper()}")

  print(f"{'─'*40}")



  # FOR 2 — percorre a lista de pratos daquela categoria

  for prato in cardapio[categoria]:



    # FOR 3 — desempacota a tupla (nome, preço, calorias) do prato

    for nome, preco, calorias in [prato]: # colchetes transforma em iterável

      print(f" {nome:22} R${preco:>5.2f} {calorias} kcal")

      total_itens += 1



      if calorias < menor_caloria[2]:

        menor_caloria = (nome, preco, calorias)



print(f"\nTotal de itens no cardápio: {total_itens}")

print(f"Opção mais leve: {menor_caloria[0]} com {menor_caloria[2]} kcal")