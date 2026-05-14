## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de Programação de computadores do curso de Ciência da computação. O objetivo do script é processar e calcular o orçamento de uma estrutura organizacional complexa (dicionários aninhados) de uma multinacional, aplicando regras de negócio dinâmicas e auditoria de execução.
 
A solução foi arquitetada utilizando conceitos avançados de Python para garantir flexibilidade, performance e rastreabilidade.
 
## 🚀 Funcionalidades
- **Cálculo Hierárquico:** Varredura completa da estrutura corporativa, independentemente do nível de profundidade.
- **Filtros Dinâmicos:** Capacidade de ignorar setores específicos e todos os seus subsetores na hora do cálculo financeiro.
- **Conversão de Câmbio:** Suporte a parâmetros opcionais para conversão de moedas em tempo de execução.
- **Sistema de Auditoria:** Monitoramento automatizado de tempo de execução e registro (logging) dos parâmetros utilizados na transação financeira.
 
## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto foi construído utilizando Python puro (Standard Library), com foco nos seguintes paradigmas e recursos:
* **Funções Recursivas (Recursion):** Utilizadas para a navegação na árvore de dados (dicionários aninhados).
* **Decorators:** Implementação do `@auditor` para injetar comportamentos de log e cronometragem sem modificar a lógica de negócios.
* **Empacotamento de Argumentos (`*args` e `**kwargs`):** Utilizados tanto no decorator quanto na função principal para permitir a passagem dinâmica de departamentos a serem ignorados e taxas de câmbio.
 
## ⚙️ Como Executar
 
### Pré-requisitos
* Python 3.8 ou superior instalado.
 
### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone https://github.com/kaiqueesantos/portfolio-kaique-vieira-santos
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd sistema-de-auditoria-de recursos-corporativos
   ```
3. Execute o script principal:
   ```bash
   python sistema_de_auditoria_de_recursos_corporativos.py
   ```
 
## 🧠 Lógica e Estrutura do Código
Breve explicação de como o código foi organizado:
* A lógica central foi baseada em uma função de soma recursiva que verifica o tipo de dado de cada entrada. Se o sistema encontra um dicionário, ele "mergulha" um nível a mais; se encontra um número, ele o soma ao total, a menos que o nome do departamento esteja na lista de exclusão passada via argumentos. O Decorator envolve essa função, capturando o tempo inicial e final através da biblioteca para gerar um relatório de performance a cada chamada.
 
* **Dados:** Os dados da empresa foram estruturados em um dicionário multinível (Matriz > Departamentos > Subdepartamentos), permitindo simular uma hierarquia corporativa real onde orçamentos estão espalhados em diferentes profundidades da estrutura.
 
## 👤 Autor
 
* **Kaique Vieira Santos**
* LinkedIn: [https://www.linkedin.com/in/kaique-santos-ab70283b5/]
* E-mail: [kaique207b@gmail.com]
 
---
*Projeto acadêmico com foco na aplicação prática de conceitos avançados da linguagem Python.*
