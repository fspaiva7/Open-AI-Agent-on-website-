from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    openai_response = get_openai_response(user_message)
    return jsonify({"reply": openai_response})

def get_openai_response(message):
    openai.api_key = 'sk-proj-ul3XW63yhuHIwEbIlCanT3BlbkFJ0luZ7AYOn0z56mhAKMXj'  # Substitua pela sua chave da API da OpenAI
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert consultant in customer pain points. Provide detailed and insightful responses to help the user. Introduce yourself as Turbo. Speak only in Portuguese."},
                {"role": "user", "content": message}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return "Erro: Não foi possível obter uma resposta válida da API da OpenAI."

if __name__ == '__main__':
    app.run(debug=True)
