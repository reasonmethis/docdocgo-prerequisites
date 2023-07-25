from flask import Flask, jsonify, request

from docdocgo import vectorstore

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    print(f"Received message: {message}")

    # Perform a dummy vectorstore query
    try:
        reply = vectorstore.as_retriever().get_relevant_documents(message)[0].page_content
    except Exception as e:
        reply = f"Error querying the vectorstore: {e}"

    print(f"Returning reply: {reply}")
    return jsonify({"content": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
