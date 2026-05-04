# Desafios de Estruturas de Dados em Python

Este repositório contém a resolução de três desafios práticos focados na manipulação de coleções complexas, utilizando loops aninhados e métodos específicos para dicionários, listas e tuplas.

## 🚀 Desafios Implementados

### 1. Criador de Emojis (Processamento de Imagem)
Implementação de um filtro de sombreamento em uma matriz RGB de 5x5 pixels[cite: 11].
*   **Lógica**: Utiliza três níveis de loops para acessar o dicionário, as linhas e os pixels individuais[cite: 11].
*   **Processamento**: Identifica pixels amarelos `(255, 255, 0)` e reduz seu brilho em 50% criando novas tuplas imutáveis[cite: 11].
*   **Arquivo**: `O_Criador_de_Emojis.py`

### 2. Matrizes Musicais (Transposição)
Algoritmo para realizar a transposição de matrizes 2x2 que representam frequências sonoras[cite: 13].
*   **Lógica**: Inverte os índices de linha por coluna ($M[i][j] \rightarrow M[j][i]$) para transformar a melodia[cite: 13].
*   **Destaque**: Uso do método `.update()` para modificar os dicionários dentro da lista de músicas[cite: 13].
*   **Arquivo**: `Matrizes_Musicais.py`

### 3. O Integrador (Cardápio de Lanchonete)
Um sistema que simula a gestão de um cardápio, integrando diversos tipos de coleções e métodos de manipulação[cite: 12].
*   **Estruturas**: 
    *   **Dicionário**: Categorias de alimentos[cite: 12].
    *   **Lista**: Itens mutáveis que permitem ordenação e destaque[cite: 12].
    *   **Tupla**: Dados fixos de cada prato (nome, preço, calorias) para evitar alterações acidentais[cite: 12].
*   **Métodos Utilizados**: `.pop()` para remover itens, `.insert()` para definir destaques e `.keys()` para navegação entre categorias[cite: 12].
*   **Arquivo**: `O_Integrador.py`

## 🛠️ Tecnologias e Conceitos Aplicados

*   **Loops Aninhados**: Acesso a dados em profundidade (Lote -> Linha -> Elemento)[cite: 11, 12, 13].
*   **Imutabilidade**: Manipulação segura de tuplas através da criação de novos objetos[cite: 11, 12].
*   **Desempacotamento**: Atribuição múltipla de valores a partir de tuplas em loops[cite: 11, 12].

---
**Desenvolvido por:** Tiago Henrique Stockmann Teixeira
