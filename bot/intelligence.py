import requests

API_URL = "https://api.example.com/chat"

def handle_query(question):

    data = {
        "message": question
    }

    try:
        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            return response.json()["response"]

    except:
        pass

    return "Não consegui gerar resposta."
