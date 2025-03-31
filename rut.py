from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Дозволити запити з різних джерел

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Повідомлення відсутнє"}), 400

    response = f"ШІ каже: {user_message}"  # Заглушка для відповіді
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5501, debug=True)
    from flask_cors import CORS
CORS(app)