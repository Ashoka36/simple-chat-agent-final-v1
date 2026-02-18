from flask import Flask, request, jsonify

app = Flask(__name__)

DEFAULT_RESPONSES = {
    "hello": "Hi! How can I help you today?",
    "how are you": "I'm doing great! Just a simple agent hosted on Render.",
    "who are you": "I am a simple chat agent built with Flask.",
    "bye": "Goodbye! Have a great day!"
}

@route('/')
def home():
    return "jsonify(s 'Simple Chat Agent is running!')

Aroute('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', "").lower()
    
    response = DEFAULT_RESPONSES.get(message, "I'm not sure how to respond to that, but I'm listening!")
    
    return jsonify({ "response": response })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
