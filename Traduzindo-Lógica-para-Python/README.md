# Trabalho de Lógica de Programação: Conversão de Pseudocódigo para Python

Este repositório contém a resolução de um trabalho acadêmico focado na transposição de algoritmos estruturados (pseudocódigos) para a linguagem Python. O objetivo foi aplicar conceitos de tipagem dinâmica, estruturas de repetição e condicionais.

## 🚀 Scripts Desenvolvidos

O trabalho consistiu na implementação de quatro funções principais, cada uma atendendo a requisitos específicos de lógica de negócio:

1.  **`processar_vendas.py`**: Calcula o total de uma compra com validação de dados e aplicação de descontos progressivos (5% para compras acima de R$ 200 e 10% acima de R$ 500).
2.  **`analisar_clima.py`**: Coleta temperaturas semanais, calcula a média e dispara alertas para condições extremas (acima de 45°C ou abaixo de -5°C).
3.  **`sistema_notas_turma.py`**: Gerencia a média de alunos de uma turma, classificando-os em "Aprovado", "Recuperação" ou "Reprovado".
4.  **`simulador_poupanca.py`**: Simula a evolução de um investimento mensal com juros compostos e aportes variáveis, monitorando metas de economia.

## 🧠 Reflexões sobre a Implementação

Após a conversão dos algoritmos, foram analisados dois pontos fundamentais da linguagem Python em comparação ao pseudocódigo:

### Questão 1: Tipagem e a função `input()`
No Python, o valor retornado pela função `input()` é sempre tratado como uma **string (texto)**. Se as funções de conversão `float()` ou `int()` forem omitidas, o Python não conseguirá realizar operações matemáticas com esses valores, resultando em erros de execução (TypeError) ou comportamentos inesperados (como a concatenação de textos em vez de soma numérica).

### Questão 2: Estruturas de Repetição e `range()`
Diferente do pseudocódigo tradicional (`PARA i DE 1 ATE 5`), onde o limite final é incluso, a função `range()` no Python é **exclusiva** no limite superior. Para que o laço execute até o número exato desejado (por exemplo, o número total de meses), a sintaxe correta deve ser `range(1, meses + 1)`. O Python adota esse comportamento para manter consistência com o fatiamento de listas e o índice inicial zero.

## 📋 Regras de Entrega Atendidas
* Implementação individual dos 4 códigos Python.
* Uso correto de tipos de dados (`float` para valores monetários/clima e `int` para contagens).
* Inclusão das respostas de reflexão teórica.

---
**Desenvolvedor:** Tiago Henrique Stockmann Teixeira
**Formação:** Analista de Infraestrutura de TI e UX Designer
