# Algoritmos de Microclima e Evacuação Espacial

Este projeto em Python está dividido em duas frentes lógicas: a análise de conforto ambiental em diferentes localidades e a simulação de tomada de decisão num cenário de evacuação.

## 🌡️ Parte 1: Algoritmo de Microclima Local

Este módulo analisa dados ambientais (Temperatura, Humidade e IQA) de locais frequentados na rotina diária, como Casa, Trabalho e Faculdade.

### Funcionalidades
* **Classificação do IQA**: Classifica a qualidade do ar em categorias: Boa (≤40), Moderada (≤80), Ruim (≤120) ou Muito Ruim.
* **Cálculo de Nota de Conforto**: Atribui uma pontuação de 0 a 10 baseada em parâmetros ideais:
    * **Temperatura Ideal**: Entre 20°C e 26°C.
    * **Humidade Ideal**: Entre 50% e 70%.
    * **Qualidade do Ar**: Penalização da nota conforme o aumento do IQA.
* **Geração de Alertas**: Emite avisos textuais sobre o estado do ambiente (ex: "Calor e ar moderado").

### Locais Monitorizados
O script processa dados de manhã e tarde para os seguintes bairros de São Paulo: **Tatuapé (Faculdade)**, **Sapopemba (Casa)** e **Moema (Trabalho)**.

---

## 🏃 Parte 2: Navegação e Evacuação Espacial

Um simulador de movimento baseado em estados de ocupação de caminhos, utilizando uma estrutura de repetição `while` para navegar por diferentes pontos de controlo.

### Lógica de Movimento
O sistema percorre uma lista de locais e decide a ação com base no estado do ambiente:

* **Livre**: O progresso é imediato.
* **Aglomeração**: O sistema alterna a estratégia de "andar" para "esperar", avançando apenas após a simulação de fluxo liberado.
* **Escada Perigosa**: Redução de velocidade para evitar quedas.
* **Corredor Cheio**: Caminhada cuidadosa para evitar colisões.

### Pontos de Evacuação
1. Sala de Aula
2. Porta da Sala
3. Escada
4. Corredor Principal
5. Saída

---

**Autor:** Tiago Henrique Stockmann Teixeira
* Analista de Infraestrutura de TI e Redes
* Estudante de UX Design
