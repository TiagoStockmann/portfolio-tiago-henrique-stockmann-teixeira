def processar_vendas():

  total_compra = 0.0

  itens_comprados = 0



  quantidade_tipos = int(input("Quantos produtos diferentes foram comprados? "))



  for i in range(1, quantidade_tipos + 1):

    nome = input("Nome do produto: ")

    preco = float(input("Preço unitário: "))

    quantidade = int(input("Quantidade deste produto: "))



    if preco <= 0 or quantidade <= 0:

      print(f"Erro: Valores inválidos para {nome}")

    else:

      subtotal = preco * quantidade

      total_compra = total_compra + subtotal

      itens_comprados = itens_comprados + quantidade



  if total_compra > 500.00:

    total_final = total_compra * 0.90

    print("Desconto de 10% aplicado!")

  elif total_compra > 200.00:

    total_final = total_compra * 0.95

  else:

    total_final = total_compra



  print(f"Resumo: {itens_comprados} itens. Total a pagar: R$ {total_final}")



processar_vendas()