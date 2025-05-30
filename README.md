# Verificador e Gerador de CPF

Este projeto em Python oferece funcionalidades para gerar CPFs (Cadastro de Pessoas Físicas) válidos e verificar a validade de CPFs existentes.

## Funcionalidades

*   **Gerar CPF:** Cria um número de CPF aleatório e válido.
*   **Validar CPF:** Verifica se um número de CPF fornecido é válido de acordo com as regras de cálculo dos dígitos verificadores.

## Como usar

1.  Clone o repositório para sua máquina local.
2.  Certifique-se de ter o Python instalado.
3.  Execute o script `main.py` no terminal:

    ```bash
    python main.py
    ```
Para clonar um repositório do GitHub e obter os códigos, siga estes passos:

1.  **Abra o Terminal:** No VS Code, vá em `Terminal` > `New Terminal`.
2.  **Navegue até o diretório desejado:** Use o comando `cd` para ir para a pasta onde você quer salvar o projeto. Por exemplo:
    ```bash
    cd C:\Users\SeuUsuario\Documentos\Projetos
    ```
    (Substitua `C:\Users\SeuUsuario\Documentos\Projetos` pelo caminho da sua pasta).
3.  **Obtenha a URL do repositório:** Vá para a página do repositório no GitHub. Clique no botão "Code" (ou "Código") e copie a URL (geralmente termina com `.git`).
4.  **Clone o repositório:** No terminal, use o comando `git clone` seguido da URL que você copiou.
    ```bash
    git clone [URL_DO_REPOSITORIO]
    ```
    (Substitua `[URL_DO_REPOSITORIO]` pela URL real do repositório do seu projeto `verificador_cpf`).
5.  **Acesse a pasta do projeto:** Após a clonagem, um novo diretório com o nome do repositório será criado. Navegue até ele:
    ```bash
    cd verificador_cpf
    ```
6.  **Execute o código:** Agora você pode executar o script Python:
    ```bash
    python main.py
    ```

Pronto! O repositório foi clonado para o seu computador e você pode executar o código.
4.  Siga as instruções no menu interativo para gerar ou validar um CPF.

## Requisitos

*   Python 3.x

## Estrutura do Código

O código está contido na classe `CPF` no arquivo `main.py`, com os seguintes métodos:

*   `verificador_cpf(cpf)`: Valida um CPF.
*   `gerador_cpf(cpf_formatado=True)`: Gera um CPF.
*   `cpf_formatar(cpf)`: Formata um CPF no padrão `xxx.xxx.xxx-xx`.

---

Este README fornece uma visão geral do projeto. Sinta-se à vontade para explorar o código para mais detalhes.
