from flask import Flask, request, jsonify, render_template
import openai
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations
                 (id INTEGER PRIMARY KEY, user_message TEXT, bot_response TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    openai_response = get_openai_response(user_message)
    store_conversation(user_message, openai_response)
    return jsonify({"reply": openai_response})

def get_openai_response(message):
    openai.api_key = 'sk-proj-RPKHkOpNXf7KaVhcFC8bT3BlbkFJv89J3iFaio9YgegUVtk8'  # Substitua pela sua chave da API da OpenAI
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return "Erro: Não foi possível obter uma resposta válida da API da OpenAI."

def store_conversation(user_message, bot_response):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO conversations (user_message, bot_response) VALUES (?, ?)",
              (user_message, bot_response))
    conn.commit()
    conn.close()

@app.route('/conversations', methods=['GET'])
def get_conversations():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT * FROM conversations")
    conversations = c.fetchall()
    conn.close()
    return jsonify(conversations)

def analyze_pain_points():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT user_message FROM conversations")
    messages = c.fetchall()
    
    pain_points = {
        "performance": 0,
        "usability": 0,
        "features": 0,
        "support": 0
    }

    for message in messages:
        if "lento" in message[0].lower() or "demora" in message[0].lower():
            pain_points["performance"] += 1
        if "difícil" in message[0].lower() or "complicado" in message[0].lower():
            pain_points["usability"] += 1
        if "falta" in message[0].lower() or "não tem" in message[0].lower():
            pain_points["features"] += 1
        if "suporte" in message[0].lower() or "ajuda" in message[0].lower():
            pain_points["support"] += 1
    
    conn.close()
    return pain_points

@app.route('/pain_points', methods=['GET'])
def get_pain_points():
    pain_points = analyze_pain_points()
    return jsonify(pain_points)



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
