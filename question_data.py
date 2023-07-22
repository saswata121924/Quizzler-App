import requests
import html

# Use the Open Trivia API to get random questions with answer type as Boolean
QUIZ_API = "https://opentdb.com/api.php"
PARAMS = {
    "amount": 10,
    "type": "boolean"
}


class Questions:
    def __init__(self):
        self.response = requests.get(url=QUIZ_API, params=PARAMS)
        data = self.response.json()
        self.quiz_data = data["results"]
        self.question_bank = [{"question": html.unescape(q["question"]), "answer": q["correct_answer"]}
                              for q in self.quiz_data]
