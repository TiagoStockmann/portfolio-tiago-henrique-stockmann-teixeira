# Sistema de Triagem de Saúde Pública

Este projeto apresenta a lógica de um sistema automatizado para triagem de pacientes em unidades de saúde, classificando o atendimento entre **Fila Prioritária** (emergencial) e **Fila Padrão** com base em critérios clínicos e demográficos.

## 📋 Funcionamento do Algoritmo

O sistema processa a entrada de dados do paciente e aplica uma série de condicionais para determinar a urgência do caso. A lógica segue o fluxo de decisão documentado nos esboços do projeto.

### Critérios de Classificação

O paciente é encaminhado para a **Fila Prioritária** se atender a pelo menos UM dos seguintes requisitos:
* **Sintomas Críticos**: Presença de sintomas considerados graves na avaliação inicial.
* **Temperatura Corporal**: Febre alta, definida como temperatura maior ou igual a **39°C**.
* **Pressão Arterial**: Identificação de pressão "Alta" ou "Baixa".
* **Faixa Etária**: Critério de prioridade legal para idosos (≥ **60 anos**) ou crianças (≤ **10 anos**).

Caso nenhum dos critérios acima seja atendido, o paciente é direcionado para a **Fila Padrão**.

## 🛠️ Especificações Técnicas

### Lógica de Decisão (Pseudocódigo)
```python
Início
    Leia sintomas_criticos, temperatura, pressão, idade
    
    Se (sintomas_criticos == "sim") então:
        Exibir "Encaminhar para FILA PRIORITÁRIA"
    Senão Se (pressao == "alta" ou pressao == "baixa") então:
        Exibir "Encaminhar para FILA PRIORITÁRIA"
    Senão Se (temperatura >= 39) então:
        Exibir "Encaminhar para FILA PRIORITÁRIA"
    Senão Se (idade >= 60 ou idade <= 10) então:
        Exibir "Encaminhar para FILA PRIORITÁRIA"
    Senão:
        Exibir "Encaminhar para FILA PADRÃO"
Fim
