# Sistema de Gerenciamento de Vestibular - FATEC Rio Claro

Este projeto é um sistema de linha de comando em Python para gerenciar o processo completo de um vestibular, desde a inscrição de candidatos até a listagem final dos aprovados. A principal característica técnica do projeto é a utilização de estruturas de dados customizadas (Listas Ligadas), construídas do zero, para todo o armazenamento e gerenciamento de informações.

## Funcionalidades Implementadas

O sistema cobre todos os requisitos de um processo seletivo simplificado:

1.  **Inscrição de Candidatos**: Cadastro de nome, CPF, curso (IA ou ESG) e status do pagamento do boleto.
2.  **Validação de Dados**: O sistema possui tratamento de erros para garantir a integridade dos dados, incluindo:
    * Nomes que devem conter apenas letras e espaços.
    * CPFs que devem conter exatamente 11 dígitos.
    * Impedimento de cadastro de CPFs duplicados.
    * Cursos que devem ser apenas 'IA' ou 'ESG'.
3.  **Cadastro de Aplicadores**: Permite criar uma lista separada para fiscais e outros aplicadores de prova.
4.  **Cálculo de Salas**: Com base no número de inscrições efetivadas, calcula automaticamente o número de salas necessárias (com capacidade de 30 alunos).
5.  **Ensalamento**: Gera e exibe a lista de candidatos distribuídos por sala.
6.  **Relatório Candidato/Vaga**: Mostra a relação de candidatos por vaga para cada curso, considerando apenas as inscrições com pagamento efetivado.
7.  **Processo de Aprovação**: Oferece um menu interativo para aprovar os candidatos um a um, respeitando o limite de 40 vagas por curso.

## Estrutura dos Arquivos

O projeto foi modularizado em quatro arquivos para promover organização e clareza:

-   `estruturas.py`: Contém as classes que definem os "modelos" de dados (`atributos_alunos`, `aplicador`, `Aprovado`). Funciona como a planta baixa do nosso sistema.
-   `gerenciador.py`: O "cérebro" do sistema. Contém a classe `gerenciador_alunos`, que implementa a lógica das listas ligadas e todas as regras de negócio.
-   `main.py`: A interface do usuário. É o arquivo que deve ser executado. Ele importa a lógica do `gerenciador.py` e apresenta um menu de linha de comando para o usuário interagir.
-   `gerador_dados.py`: Uma ferramenta auxiliar para criar dados de teste em massa usando a biblioteca `Faker`. Ele gera um arquivo `vestibulandos.csv` que pode ser carregado pelo sistema.

## Como Usar o Sistema

### Pré-requisitos

É necessário ter o Python 3 instalado e a biblioteca `Faker`. Para instalar o Faker, execute no seu terminal:
```bash
pip install Faker