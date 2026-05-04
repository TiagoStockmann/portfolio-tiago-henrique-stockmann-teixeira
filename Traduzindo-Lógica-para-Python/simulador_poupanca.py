def simulador_poupanca():

  saldo = float(input("Valor inicial do investimento: "))

  taxa = float(input("Taxa de juros mensal (em %): "))

  meses = int(input("Número de meses da simulação: "))



  for i in range(1, meses + 1):

    aporte = float(input(f"Quanto deseja depositar no mês {m}? (0 para nenhum) "))



    saldo = saldo + aporte

    juros = saldo * (taxa / 100)

    saldo = saldo + juros



    print(f"Mês {i}: Saldo atualizado = R${saldo:.2f}")



    if saldo > 10000.0:

      print(f"Parabéns! Você atingiu a meta de 10k no mês {i}")



  print(f"Resultado final após {meses} meses: R$ {saldo:.2f}")



simulador_poupanca()