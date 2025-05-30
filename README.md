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
