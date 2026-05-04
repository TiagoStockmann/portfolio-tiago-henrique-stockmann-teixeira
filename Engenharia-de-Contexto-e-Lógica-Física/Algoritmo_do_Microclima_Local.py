#Parte 1: O Algoritmo do Microclima Local (Casa, Trabalho, Faculdade),


def classificar_iqa(iqa):

  match iqa:

    case _ if iqa <= 40:

      return "Boa"

    case _ if iqa <= 80:

      return "Moderada"

    case _ if iqa <= 120:

      return "Ruim"

    case _:

      return "Muito Ruim"



def calcular_conforto(temp, umidade, iqa):

  nota = 10



  # Temperatura ideal

  if temp < 20 or temp > 26:

    nota = nota - 2



  # Umidade ideal

  if umidade < 50 or umidade > 70:

    nota = nota - 2



  # Qualidade do ar

  if iqa > 80:

    nota = nota - 3

  elif iqa > 40:

    nota = nota - 1



  if nota < 0:

    nota = 0



  return nota



def gerar_alerta(temp, iqa):

  if temp > 25 and iqa > 40:

    return "Calor e ar moderado."

  elif temp > 25:

    return "Temperatura alta."

  elif iqa > 40:

    return "Qualidade do ar moderada."

  else:

    return "Ambiente agradável."



def analisar_microclima():

  dados = [

    ["Faculdade (Tatuapé) - Manhã", 20, 78, 35],

    ["Faculdade (Tatuapé) - Tarde", 26, 52, 55],

    ["Casa (Sapopemba) - Manhã", 19, 82, 40],

    ["Casa (Sapopemba) - Tarde", 27, 50, 60],

    ["Trabalho (Moema) - Manhã", 21, 75, 30],

    ["Trabalho (Moema) - Tarde", 28, 48, 45]

  ]



  for local in dados:

    nome = local[0]

    temp = local[1]

    umidade = local[2]

    iqa = local[3]



    qualidade = classificar_iqa(iqa)

    conforto = calcular_conforto(temp, umidade, iqa)

    alerta = gerar_alerta(temp, iqa)



    print(30 * "=")

    print("Local:", nome)

    print("Temperatura:", temp, "°C")

    print("Umidade:", umidade, "%")

    print("IQA:", iqa)

    print("Qualidade do ar:", qualidade)

    print("Nota de conforto:", conforto)

    print(alerta)

    print(30 * "=")



analisar_microclima()



#Parte 2: Navegação e Evacuação Espacial



locais = [

  "Sala de Aula",

  "Porta da Sala",

  "Escada",

  "Corredor Principal",

  "Saída"

]



estados = [

  "livre",

  "aglomeração",

  "escada_perigosa",

  "corredor_cheio",

  "saida"

]





def simular_evacuacao():



  posicao = 0

  estrategia = "andar"



  print("=== SIMULAÇÃO DE EVACUAÇÃO ===\n")



  while posicao <= 4:



    local_atual = locais[posicao]

    estado_atual = estados[posicao]



    print("Local atual:", local_atual)



    if estado_atual == "livre":

      print("Caminho livre. Avançando.\n")

      posicao = posicao + 1



    elif estado_atual == "aglomeração":



      print("Há muitas pessoas na passagem.")



      if estrategia == "andar":

        print("Esperando o fluxo diminuir.\n")

        estrategia = "esperar"



      else:

        print("Passagem liberada. Avançando.\n")

        posicao = posicao + 1



    elif estado_atual == "escada_perigosa":

      print("Escada perigosa. Descendo devagar para evitar queda.\n")

      posicao = posicao + 1



    elif estado_atual == "corredor_cheio":

      print("Corredor cheio. Caminhando com cuidado para evitar trombadas.\n")

      posicao = posicao + 1



    elif estado_atual == "saida":

      print("Saída alcançada com sucesso!")

      break





simular_evacuacao(locais) = [

  "Sala de Aula",

  "Porta da Sala",

  "Escada",

  "Corredor Principal",

  "Saída"

]



estados = [

  "livre",

  "aglomeração",

  "escada_perigosa",

  "corredor_cheio",

  "saida"

]





def simular_evacuacao():



  posicao = 0

  estrategia = "andar"



  print("=== SIMULAÇÃO DE EVACUAÇÃO ===\n")



  while posicao <= 4:



    local_atual = locais[posicao]

    estado_atual = estados[posicao]



    print("Local atual:", local_atual)



    if estado_atual == "livre":

      print("Caminho livre. Avançando.\n")

      posicao = posicao + 1



    elif estado_atual == "aglomeração":



      print("Há muitas pessoas na passagem.")



      if estrategia == "andar":

        print("Esperando o fluxo diminuir.\n")

        estrategia = "esperar"



      else:

        print("Passagem liberada. Avançando.\n")

        posicao = posicao + 1



    elif estado_atual == "escada_perigosa":

      print("Escada perigosa. Descendo devagar para evitar queda.\n")

      posicao = posicao + 1



    elif estado_atual == "corredor_cheio":

      print("Corredor cheio. Caminhando com cuidado para evitar trombadas.\n")

      posicao = posicao + 1



    elif estado_atual == "saida":

      print("Saída alcançada com sucesso!")

      break





simular_evacuacao()