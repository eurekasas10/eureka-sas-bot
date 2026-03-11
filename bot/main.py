from intelligence import handle_query

while True:

    question = input("Digite uma pergunta: ")

    answer = handle_query(question)

    print("Resposta:", answer)
