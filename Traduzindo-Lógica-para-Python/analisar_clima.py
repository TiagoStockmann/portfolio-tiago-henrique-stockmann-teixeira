def analisar_clima():

  soma_temperaturas = 0.0

  dias_quentes = 0

  alerta_extremo = False



  for i in range(1, 8):

    temp = float(input(f"Digite a temperatura do dia {i}: "))

    soma_temperaturas = soma_temperaturas + temp



    if temp > 35.0:

      dias_quentes = dias_quentes + 1



    if temp > 45.0 or temp < -5.0:

      alerta_extremo = True



  media = soma_temperaturas / 7

  print(f"Média semanal: {media}")

  print(f"Dias acima de 35°C: {dias_quentes}")



  if alerta_extremo == True:

    print("CUIDADO: Condições climáticas perigosas detectadas!")

  else:

    print("Clima dentro da normalidade operacional.")



analisar_clima()