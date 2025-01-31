# Visão Geral do Projeto

O projeto **Geração de Dados Fictícios** tem como objetivo criar um conjunto de tabelas simulando um ambiente de dados empresariais (modelo dimensional), ideal para treinar habilidades de ETL, modelagem de dados e construção de dashboards (ex.: Power BI).

## Objetivos

1. Demonstrar conhecimentos de **CRISP-DM** na geração de dados:
   - **Entendimento do Negócio**: Criar um cenário fictício de contratos, clientes, fornecedores, pagamentos e violações.
   - **Entendimento dos Dados**: Definir atributos de dimensões e fatos.
   - **Preparação dos Dados**: Utilizar Python e a biblioteca Faker para gerar dados coerentes.
   - **Modelagem**: Criar tabelas fato e dimensão.
   - **Avaliação**: Validar a consistência entre tabelas e chaves (ID_Cliente, ID_Contrato, etc.).
   - **Implantação**: Disponibilizar os CSVs e facilitar a integração com ferramentas de BI.

2. Permitir a construção de relatórios e dashboards em ferramentas como Power BI, Tableau, ou Google Data Studio.

3. Servir como portfólio para demonstrar habilidades em:
   - Python (Faker, pandas, organização de códigos).
   - Modelagem dimensional (fatos e dimensões).
   - Documentação e boas práticas.

## Metodologia

Este projeto segue a metodologia **CRISP-DM**, adaptada para a geração de dados fictícios:

1. **Entendimento do Negócio**: Identificar as necessidades fictícias do cenário, como contratos e pagamentos entre empresas.
2. **Entendimento dos Dados**: Planejar as tabelas, chaves primárias, chaves estrangeiras e atributos relevantes.
3. **Preparação dos Dados**: Implementar funções Python para gerar tabelas com volumes adequados.
4. **Modelagem**: Garantir consistência entre tabelas e validar relações lógicas (fatos e dimensões).
5. **Avaliação**: Verificar se os dados gerados atendem aos objetivos do projeto.
6. **Implantação**: Disponibilizar os dados em CSV e integrar às ferramentas de BI para visualização.

## Estrutura das Tabelas

### Dimensões

- **Dim_Clientes**: Dados de clientes, incluindo ID, nome, segmento, localização e tamanho.
- **Dim_Fornecedores**: Dados de fornecedores, como ID, nome, localização e categoria.
- **Dim_Profissionais**: Informações de profissionais vinculados aos contratos.
- **Dim_Tipo_Contrato**: Tipos de contrato, como fornecimento, locação, serviços, etc.
- **Dim_Tipo_Pagamento**: Métodos de pagamento disponíveis.
- **Dim_Tipo_Violacao**: Classificação de violações contratuais.

### Fatos

- **Fato_Contratos**: Registros de contratos, incluindo cliente, fornecedor, tipo de contrato, valores, datas e status.
- **Fato_Pagamentos**: Detalhes de pagamentos vinculados a contratos.
- **Fato_Violacoes**: Ocorrências de violações contratuais registradas.

## Utilização do Projeto

O resultado deste projeto são tabelas CSV que podem ser integradas diretamente em ferramentas de BI para:

- Análise de pagamentos e inadimplência.
- Identificação de padrões de violações contratuais.
- Relatórios de desempenho de fornecedores e clientes.

Consulte o arquivo [README.md](../README.md) para instruções detalhadas sobre a execução do projeto.