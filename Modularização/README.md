# Sistema de Caixa e Decomposição de Troco (Modularizado)

Este projeto apresenta a estrutura lógica e o pseudocódigo para um sistema de frente de caixa, focado na modularização de processos como validação de pagamento, cálculo de valores e distribuição de cédulas para o troco.

## 🏗️ Estrutura de Modularização

[cite_start]O sistema foi desenhado de forma modular para garantir a separação de responsabilidades entre as funções[cite: 70]:

### 1. Validação de Pagamento (`validar_pagamento`)
[cite_start]Responsável por verificar se o valor entregue pelo cliente é suficiente para cobrir o custo da compra[cite: 19, 60].
* [cite_start]**Entrada**: `Valor_compra`, `Valor_pago`[cite: 19].
* [cite_start]**Lógica**: Retorna `VERDADEIRO` se o pagamento for maior ou igual à compra, caso contrário, retorna `FALSO`[cite: 21, 23, 25].

### 2. Cálculo de Troco (`calcular_troco`)
[cite_start]Realiza a operação aritmética básica para determinar o saldo devido ao cliente[cite: 29, 66].
* [cite_start]**Operação**: `Troco = Valor_pago - Valor_compra`[cite: 32, 68].

### 3. Decomposição de Notas (`decompor_notas`)
[cite_start]Módulo que processa o valor do troco e o divide nas cédulas disponíveis[cite: 48, 53].
* [cite_start]**Cédulas Disponíveis**: R$ 100, R$ 50, R$ 10, R$ 5 e R$ 1[cite: 4, 54].
* [cite_start]**Lógica**: Utiliza as operações `DIV` (divisão inteira) para quantificar as notas e `MOD` (resto da divisão) para atualizar o saldo do troco restante[cite: 9, 11, 55].

## 💻 Fluxo do Programa Principal (`SistemaCaixa`)

[cite_start]O programa principal coordena a interação com o usuário e a chamada dos módulos[cite: 35, 36]:

1.  [cite_start]**Entrada de Dados**: Solicita o valor da compra e o valor pago[cite: 38, 40].
2.  **Verificação**: Chama o módulo de validação. [cite_start]Se o pagamento for insuficiente, o sistema exibe um erro e encerra[cite: 42, 44, 45].
3.  **Processamento**:
    * [cite_start]Calcula o valor exato do troco[cite: 47].
    * [cite_start]Gera a lista de notas necessárias para o troco através da função de decomposição[cite: 48].
4.  [cite_start]**Saída (Recibo)**: Exibe o resumo da compra, o valor pago, o troco total e a lista detalhada de cédulas[cite: 49, 50, 85].

## 📐 Lógica de Decomposição (Exemplo)

[cite_start]O algoritmo de notas funciona de forma iterativa para cada denominação na lista[cite: 6]:

* [cite_start]**Condição**: Se o `Troco >= nota`[cite: 8].
* [cite_start]**Quantidade**: `quantidade = Troco DIV nota`[cite: 9].
* [cite_start]**Atualização**: `Troco = Troco MOD nota`[cite: 11].

---
**Documentação baseada nos manuscritos de lógica de programação.**
* **Autor:** Tiago Henrique Stockmann Teixeira
* **Contexto:** Analista de Infraestrutura e Redes
