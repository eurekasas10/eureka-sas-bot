import requests

def analyze_question(question):
    return question

def generate_response(question):

    # Aqui você poderia enviar a pergunta para uma IA
    # Por enquanto vamos só responder perguntas simples

    question = question.lower()

    if "capital" in question and "frança" in question:
        return "A capital da França é Paris."

    if "2+2" in question:
        return "2 + 2 = 4"

    return "Ainda não sei responder essa pergunta."

def handle_query(query):
    question = analyze_question(query)
    return generate_response(question)
