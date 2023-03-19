import openai
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

with open("api_key.txt", "r") as apiFile:
    apiKey = apiFile.readline()
    openai.api_key = apiKey


app = Flask(__name__)
CORS(app)
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    gpt_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"User: {user_message}\nAI:",
        temperature=0.8,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["User:"]
    )

    ai_message = gpt_response.choices[0].text.strip()
    return jsonify({'message': ai_message})

if __name__ == '__main__':
    app.run(debug=True)
