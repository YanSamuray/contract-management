# Projeto de Geração de Dados Fictícios

Este repositório contém o código, dados e documentação relacionados ao projeto de **geração de dados fictícios** para fins de demonstração em portfólio (por exemplo, em dashboards de Power BI). A geração de dados segue um modelo dimensional (fatos e dimensões) e é inspirada na metodologia CRISP-DM.

## Sumário

- [Visão Geral do Projeto](docs/project_overview.md)
- [Guia de Instalação](docs/installation_guide.md)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Estrutura do Repositório

- **`data/`**  
  Diretório para armazenamento de dados gerados (CSV). Pode ser subdividido em:
  - `raw/`: Dados brutos (se você decidir manter algum dado inicial ou de referência).
  - `output/`: Local onde os CSVs finais são salvos.

- **`scripts/`**  
  Código-fonte Python:
  - `dims/`: Scripts responsáveis pela geração das dimensões (ex.: `dim_clientes.py`, `dim_fornecedores.py`, etc.).
  - `fatos/`: Scripts responsáveis pela geração das tabelas fato (ex.: `fato_contratos.py`, `fato_pagamentos.py`, etc.).
  - `main.py`: Script principal que orquestra toda a geração e salva os dados em `data/output`.

- **`docs/`**  
  Documentação detalhada:
  - [project_overview.md](docs/project_overview.md): Descrição geral do projeto, metodologia (CRISP-DM), objetivos, etc.
  - [installation_guide.md](docs/installation_guide.md): Passos para configurar o ambiente e executar o projeto.

- **`tests/`** (opcional)  
  Testes automatizados para validar scripts e dados (ex.: teste de chaves únicas, integridade referencial, etc.).

- **`models/`** (opcional)  
  Caso você decida criar algum tipo de modelo (ML ou estatístico) em cima dos dados gerados.

- **`requirements.txt`**  
  Lista de dependências do projeto (pandas, Faker, etc.).

- **`README.md`**  
  Este documento, com as informações gerais e de referência.

## Contribuição

Contribuições são bem-vindas! Se desejar abrir uma *issue* ou propor *pull requests*, fique à vontade para melhorar o código ou a documentação.  
- Para instruções detalhadas sobre o fluxo de contribuição, consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) (caso exista).

## Licença

Este projeto está sob a licença [MIT](LICENSE) (ou outra que você escolher).  
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Em caso de dúvidas, sugestões ou feedback:

**Yan Samuray**  
E-mail: [yansamuray@gmail.com](mailto:yansamuray@gmail.com)