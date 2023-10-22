from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- New import
import openai

app = Flask(__name__)
CORS(app)  # <-- This will enable CORS for all routes

# Initialize OpenAI with your API key
openai.api_key = "ENTER_YOUR_KEY"


@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    print(data)
    query = "You are tax expert. Answer the below query: "+ str(data.get('query')+" Remeber  If the query is doesn't ask about taxes just tell them you are tax assistant and can only help with it. t must that you follow this restriction")

    if not query:
        return jsonify({"error": "Query is required."}), 400

    try:
        response = openai.Completion.create(
             engine= "gpt-3.5-turbo-instruct",
            prompt=query,
            max_tokens=3500
        )
        response_text = response.choices[0].text.strip()
        return jsonify({"response": response_text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "API call failed"}), 500

if __name__ == "__main__":
    app.run(port=3001)

