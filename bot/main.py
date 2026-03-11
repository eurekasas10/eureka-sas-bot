import time

class Bot:
    def __init__(self, question_func, process_func, answer_func, interval=60):
        self.question_func = question_func
        self.process_func = process_func
        self.answer_func = answer_func
        self.interval = interval

    def run(self):
        while True:
            question = self.question_func()
            if question:
                answer = self.process_func(question)
                self.answer_func(answer)
            time.sleep(self.interval)

# Example question, processing, and answering functions

def read_question():
    # Logic to read a question (placeholder)
    return "What is the capital of France?"


def process_question(question):
    # Logic to process the question (placeholder)
    return "The capital of France is Paris."


def submit_answer(answer):
    # Logic to submit the answer (placeholder)
    print(answer)

if __name__ == '__main__':
    bot = Bot(read_question, process_question, submit_answer, interval=10)
    bot.run()