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
- chatbot.db # Arquivo do banco de dados SQLite


## Funcionalidades Principais

- **Página Web Interativa**: Interface de usuário simples e intuitiva.
- **Chatbot**: Integrado com a API da OpenAI para gerar respostas.
- **Armazenamento de Conversas**: Conversas são armazenadas em um banco de dados SQLite.
- **Análise de Dores**: Análise das dores dos clientes com base nas mensagens armazenadas.

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

4. Crie um arquivo `.env` e adicione sua chave de API da OpenAI:
    ```text
    OPENAI_API_KEY=your_openai_api_key
    ```

### Executando o Projeto, Interaja com o chatbot e verifique as novas rotas:

1. Inicie o servidor Flask:
    ```bash
    python app.py
    ```

2. Acesse o aplicativo em:
    ```text
    http://127.0.0.1:5000
    ```

3. Para visualizar a análise de dores: 
  ```text
  http://127.0.0.1:5000/pain_points
  ```

## Estrutura de Código

### `app.py`

Este é o arquivo principal que configura o servidor Flask, a integração com a API da OpenAI e o armazenamento de conversas no banco de dados SQLite.

### `templates/index.html`

Arquivo HTML que define a interface do usuário.

### `static/styles.css`

Arquivo CSS para estilizar a página web.

### `requirements.txt`

Arquivo que lista todas as dependências do projeto.

## Customização do Chatbot (Prompt Engineering)

Você pode ajustar o comportamento do chatbot modificando o prompt do sistema no arquivo `app.py`:

```python
response = openai.Completion.create(
    engine="davinci-codex",  # Ajuste o motor se necessário
    prompt=message,
    max_tokens=150,
    temperature=0.7,
)
```

## Funcionalidades Adicionais

# Armazenamento de Conversas
As mensagens dos usuários e as respostas do chatbot são armazenadas em um banco de dados SQLite.

# Análise de Dores
Um método básico de análise que categoriza as dores dos clientes com base em palavras-chave nas mensagens.

# Rotas Adicionais
/conversations: Recupera e exibe as conversas armazenadas no banco de dados.
/pain_points: Visualiza a análise das dores dos clientes.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.


