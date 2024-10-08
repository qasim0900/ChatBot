import os
from dotenv import load_dotenv
from chatbot import ChatGPTBotAPI
from flask import Flask, request, jsonify

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
print("API",api_key)
bot_api = ChatGPTBotAPI(api_key=api_key)

# -------------------------------
# :: Create Prompt Function
# -------------------------------

""" 
The create_prompt function handles POST requests to "/prompts," 
returning a 400 error if no prompt is provided or a 201 response with the prompt's index if successful.
"""


@app.route("/prompts", methods=["POST"])
def create_prompt():
    data = request.json
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    index = bot_api.create_prompt(prompt)
    return jsonify({"index": index}), 201


# -------------------------------
# :: Get Response Function
# -------------------------------

""" 
The get_response function retrieves a prompt's response by index via a GET request, 
returning a 200 response or a 404 error if the index is invalid.
"""


@app.route("/prompts/<int:prompt_index>/response", methods=["GET"])
def get_response(prompt_index):
    try:
        response = bot_api.get_response(prompt_index)
        return jsonify({"response": response}), 200
    except IndexError:
        return jsonify({"error": "Prompt index out of range"}), 404


# -------------------------------
# :: Update Prompt Function
# -------------------------------

""" 
The update_prompt function updates a prompt via a PUT request, returning a 400 error if the new prompt is missing,
a 200 success message, or a 404 error if the index is invalid.
"""


@app.route("/prompts/<int:prompt_index>", methods=["PUT"])
def update_prompt(prompt_index):
    data = request.json
    new_prompt = data.get("prompt")
    if not new_prompt:
        return jsonify({"error": "New prompt is required"}), 400
    try:
        bot_api.update_prompt(prompt_index, new_prompt)
        return jsonify({"message": "Prompt updated"}), 200
    except IndexError:
        return jsonify({"error": "Prompt index out of range"}), 404


if __name__ == "__main__":
    app.run(debug=True)
