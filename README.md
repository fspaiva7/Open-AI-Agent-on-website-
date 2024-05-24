# Chatbot PoC com Flask e OpenAI

Este projeto é uma prova de conceito (PoC) de um chatbot que utiliza Flask para o backend e a API da OpenAI para gerar respostas baseadas nas entradas do usuário. O objetivo é criar uma interface web simples onde os usuários podem interagir com um chatbot que responde às suas perguntas.

## Estrutura do Projeto

my_project/
- app.py
- requirements.txt
- templates
    - index.html
- static
    - styles.css




## Funcionalidades Principais

- **Página Web Interativa**: Interface de usuário simples e intuitiva.
- **Chatbot**: Integrado com a API da OpenAI para gerar respostas.
- **Prompt Engineering**: Possibilidade de ajustar o comportamento do chatbot através de prompts.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.7 ou superior
- Virtualenv

### Instalação

1. Suba os arquivos seguindo a estrutura acima. 
  

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Executando o Projeto

1. Inicie o servidor Flask:
    ```bash
    python app.py
    ```

2. Acesse o aplicativo em:
    ```text
    http://127.0.0.1:5000
    ```

## Estrutura de Código

### `app.py`

Este é o arquivo principal que configura o servidor Flask e a integração com a API da OpenAI.

### `templates/index.html`

Arquivo HTML que define a interface do usuário.

### `static/styles.css`

Arquivo CSS para estilizar a página web.

### `requirements.txt`

Arquivo que lista todas as dependências do projeto.

## Customização do Chatbot (Prompt Engineering)

Você pode ajustar o comportamento do chatbot modificando o prompt do sistema no arquivo `app.py`:

```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ],
    max_tokens=150,
    temperature=0.7,
)
