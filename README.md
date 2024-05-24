# Open-AI-Agent-on-website-
Open AI Agent on website 
# Chatbot Interativo com Flask e OpenAI

Este projeto é um chatbot interativo desenvolvido com Flask que utiliza a API da OpenAI para gerar respostas. O chatbot é configurado para atuar como um consultor digital especializado em identificar as dores dos clientes e fornecer respostas detalhadas e perspicazes.

## Funcionalidades

- **Interface Web Interativa**: Uma página web simples com um chatbox onde os usuários podem enviar mensagens e receber respostas do chatbot.
- **Integração com OpenAI**: Utiliza o modelo `gpt-3.5-turbo` da OpenAI para processar as mensagens dos usuários e gerar respostas.
- **Engenharia de Prompt**: O chatbot é configurado com prompts específicos para orientar suas respostas, se apresentando como um consultor digital da empresa 'Ser + Digital' e respondendo em português.
- **Armazenamento de Conversas**: As mensagens trocadas entre o usuário e o chatbot são armazenadas em um banco de dados SQLite para posterior análise.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # No Windows
    # source venv/bin/activate  # No macOS/Linux
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração

1. Obtenha uma chave de API da OpenAI e substitua `'YOUR_OPENAI_API_KEY'` no arquivo `app.py` pela sua chave de API.

2. Inicie o banco de dados:
    ```bash
    python app.py
    ```

## Execução

1. Execute a aplicação Flask:
    ```bash
    python app.py
    ```

2. Abra o navegador e acesse `http://127.0.0.1:5000` para interagir com o chatbot.

## Estrutura do Projeto

my_project/
│
├── templates/
│ └── index.html
├── static/
│ └── styles.css
├── app.py
├── chatbot.db
├── requirements.txt
└── README.md
