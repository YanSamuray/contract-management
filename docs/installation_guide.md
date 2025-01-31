# Guia de Instalação

Este documento descreve como configurar o ambiente de desenvolvimento para executar o projeto de **geração de dados fictícios**.

## Pré-requisitos

- **Conda** instalado. Para instalação, consulte o [Guia Oficial](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

## Configuração do Ambiente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/YanSamuray/contract-management.git
   cd contract-management
   ```

2. **Crie ou atualize o ambiente Conda:**
   Se o ambiente ainda não foi criado, execute:
   ```bash
   conda env create -f environment.yml
   ```
   Caso o ambiente já exista e precise ser atualizado:
   ```bash
   conda env update --file environment.yml --prune
   ```
   
3. **Ative o ambiente:**
   ```bash
   conda activate geracao_ficticios
   ```

4. **Execute o script principal** (para gerar os CSVs):
   ```bash
   python scripts/main.py
   ```

5. **Verifique os resultados:**
   - Os arquivos CSV serão gerados na pasta `data/output` (caso siga a estrutura sugerida).

## Problemas Comuns

- **Erro ao criar o ambiente:** Certifique-se de que o Conda está instalado corretamente e atualizado.
- **Dependências desatualizadas:** Se houver pacotes incompatíveis, tente remover o ambiente e recriá-lo com:
   ```bash
   conda env remove -n geracao_ficticios
   conda env create -f environment.yml
   ```
- **Encoding de CSV:** Caso encontre problemas de encoding, verifique se está usando `UTF-8` ou configure outro encoding desejado.
- **Permissões em pastas:** Em alguns sistemas, pode ser necessário conceder permissões de escrita na pasta `data/output`.

## Recursos Adicionais

- [Documentação oficial do Python](https://docs.python.org/3/)
- [Documentação oficial do Conda](https://docs.conda.io/)
- Consulte o arquivo [README.md](../README.md) para mais detalhes sobre a estrutura do repositório.
- Entre em contato pelo email: [yansamuray@gmail.com](mailto:yansamuray@gmail.com)