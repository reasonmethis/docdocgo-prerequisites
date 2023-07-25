import flask
import requests
import functions_framework
from google.cloud import firestore

# TODO Set to the correct URL of the business logic flask API 
BUSINESS_LOGIC_API_URL = "http://<PUT THE URL HERE OR IN ENV VAR>:8000/chat" # must end with /chat

db = firestore.Client()


@functions_framework.http
def get_chat_response(req: flask.Request):
    request_json = req.get_json(silent=True)

    if request_json["type"] != "MESSAGE":
        return {}

    msg_json = request_json.get("message", {})
    msg_text = msg_json.get("argumentText", "")

    # Test ability to interact with business logic API
    response_data = requests.post(BUSINESS_LOGIC_API_URL, json={"message": msg_text})

    if response_data.status_code == 200:
        response = response_data.json()
    else:
        response = {
            "content": f"Error getting response (status code {response_data.status_code}).",
        }

    print(f"Response: {response}")

    # Test ability to save data to Firestore
    db.collection("test").add({"message": msg_text})

    return {
        "text": "I received this response from the business logic API:"
        f"\n\n{response['content']}"
        "\n\nI was also able to save data to Firestore."
        "\n\nIf the above API response is a chunk of one of the Confluence pages, then everything is working!"
    }
