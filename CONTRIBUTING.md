# Guia de Contribuição

Obrigado por seu interesse em contribuir para este projeto de **Geração de Dados Fictícios**! Este guia descreve as etapas para colaborar com código, documentação ou relatórios de problemas.

## Como Contribuir

### 1. Reportar Problemas

Se você encontrou um bug, problema ou tem uma sugestão de melhoria, siga estas etapas:

1. Verifique se o problema já foi relatado, navegando até a página de *Issues* do repositório.
2. Caso não tenha sido relatado, abra uma nova *Issue* com as seguintes informações:
   - **Descrição clara do problema**
   - **Passos para reproduzir o problema**
   - Logs ou mensagens de erro, se aplicável

### 2. Melhorar a Documentação

A documentação é fundamental para manter o projeto acessível e organizado. Contribuições para melhorar o *README.md*, guias ou outros arquivos de documentação são bem-vindas.

1. Edite o arquivo correspondente (ex.: `docs/project_overview.md`).
2. Proponha sua alteração via um *pull request* (veja abaixo como fazer).

### 3. Contribuir com Código

#### Passo a Passo

1. **Faça um Fork** do repositório:

   - Clique no botão "Fork" no canto superior direito do repositório.
   - Clone seu fork localmente:
     ```bash
     git clone https://github.com/YanSamuray/contract-management.git
     cd contract-management
     ```

2. **Crie uma Branch para sua contribuição:** Escolha um nome descritivo para sua branch:

   ```bash
   git checkout -b minha-contribuicao
   ```

3. **Faça suas alterações no código ou na documentação.**

4. **Teste suas alterações:** Verifique se tudo está funcionando como esperado e se você não introduziu novos problemas.

5. **Commit e Push:** Certifique-se de criar commits claros e descritivos:

   ```bash
   git add .
   git commit -m "Descrição clara da alteração"
   git push origin minha-contribuicao
   ```

6. **Abra um Pull Request:**

   - Navegue até o repositório original no GitHub.
   - Clique em "Pull Request" e selecione sua branch.
   - Inclua uma descrição clara das alterações e do motivo da contribuição.

#### Padrões de Código

- Use Python 3.x.
- Siga o *PEP 8* (estilo de código para Python).
- Certifique-se de que as funções e variáveis tenham nomes claros e significativos.
- Documente suas funções usando docstrings.

#### Testes

Se você adicionou ou alterou funcionalidades, crie testes para garantir a estabilidade do código. Armazene os testes na pasta `tests/`.

## Código de Conduta

Este projeto adota um [código de conduta](CODE_OF_CONDUCT.md) para garantir um ambiente acolhedor e respeitoso para todos. Leia o arquivo correspondente antes de contribuir.

## Dúvidas?

Entre em contato pelo email: [yansamuray@gmail.com](mailto:yansamuray@gmail.com). Obrigado por contribuir!

