from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def chatbot_response(user_input):
    responses = {
        "hello": "Hi! How can I help you?",
        "hi": "Hello! What’s up?",
        "how are you": "I’m good 😊, how are you?",
        "bye": "Goodbye! Have a nice day 👋",
    }
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I don't understand that.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.json["message"]
    response = chatbot_response(user_message)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
