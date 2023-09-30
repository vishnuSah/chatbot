import json
import random
import nltk
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

nltk.download('punkt')


with open('intents.json', 'r') as file:
    intents = json.load(file)


intent_names = [intent['name'] for intent in intents['intents']]
intent_examples = {intent['name']: intent['examples'] for intent in intents['intents']}
intent_responses = {intent['name']: intent['responses'] for intent in intents['intents']}


def recognize_intent(user_input):
    user_words = nltk.word_tokenize(user_input.lower())
    for intent, examples in intent_examples.items():
        for example in examples:
            example_words = nltk.word_tokenize(example.lower())
            if any(word in user_words for word in example_words):
                return intent
    return None


def get_random_response(intent):
    return random.choice(intent_responses[intent])


@app.route('/')
def chat_ui():

    return render_template('chatbot.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    intent = recognize_intent(user_message)
    
    if intent:
        response = get_random_response(intent)
    else:
        response = "I'm sorry, I didn't understand that."
    
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)