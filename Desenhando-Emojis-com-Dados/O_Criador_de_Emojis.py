emoji_data = {

  "nome": "Smile",

  "grade": [

    [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)], # topo

    [(255,255,0), (0,0,0),  (255,255,0), (0,0,0),  (255,255,0)], # olhos

    [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)], # meio

    [(255,255,0), (0,0,0),  (0,0,0),  (0,0,0),  (255,255,0)], # boca

    [(255,255,0), (255,255,0), (255,255,0), (255,255,0), (255,255,0)], # base

  ]

}



AMARELO = (255,255,0)

grade_com_sombra = []



for chave, valor in emoji_data.items():

 if chave != "grade":

  continue

 for numero_linha, linha in enumerate(valor):

  linha_processada = []



  for pixel in linha:

   if pixel == AMARELO:

    r, g ,b = pixel

    pixel_escuro = (r // 2, g // 2, b // 2)

    linha_processada.append(pixel_escuro)

   else:

    linha_processada.append(pixel)

  grade_com_sombra.append(linha_processada)

  print(f" linha {numero_linha}:", linha_processada)



emoji_data["grade"] = grade_com_sombra

print("Filtro aplicado")