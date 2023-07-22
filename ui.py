import random
from tkinter import *
from question_data import Questions

THEME_COLOUR = "#375562"


# Create the UI for the Quizzler App
class QuizScreen:

    def __init__(self):
        self.question_bank = Questions().question_bank
        self.score = 0
        self.hs = 0
        self.screen = Tk()
        self.screen.title("Quizzler")
        self.screen.config(pady=20, padx=20, bg=THEME_COLOUR)
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOUR, font=("arial", 12, "normal"))
        self.score_label.grid(row=0, column=1, pady=10)
        self.high_score()
        self.high_score_label = Label(text=f"High Score: {self.hs}",
                                      fg="white", bg=THEME_COLOUR, font=("arial", 12, "normal"))
        self.high_score_label.grid(row=0, column=0, pady=10)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_dict = random.choice(self.question_bank)
        self.question = self.question_dict["question"]
        self.correct_answer = self.question_dict["answer"]
        self.question_text = self.canvas.create_text(
            150, 125, text=f"{self.question}", width=250, font=("arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=10)
        self.correct_image = PhotoImage(file="images/true.png")
        self.button1 = Button(image=self.correct_image, highlightthickness=0, borderwidth=0, command=self.answer_true)
        self.button1.grid(row=2, column=0, pady=10)
        self.wrong_image = PhotoImage(file="images/false.png")
        self.button2 = Button(image=self.wrong_image, highlightthickness=0, borderwidth=0, command=self.answer_false)
        self.button2.grid(row=2, column=1, pady=10)
        self.screen.mainloop()

    # Check if the answer is True
    def answer_true(self):
        if self.correct_answer == "True":
            self.update_score()
        else:
            self.canvas.config(bg="#ff751a")
        self.screen.after(ms=600, func=self.change_question)

    # Check if the answer is False
    def answer_false(self):
        if self.correct_answer == "False":
            self.update_score()
        else:
            self.canvas.config(bg="#ff751a")
        self.screen.after(ms=600, func=self.change_question)

    # Update the score on every correct answer
    def update_score(self):
        self.canvas.config(bg="light green")
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

    def change_question(self):
        self.canvas.config(bg="white")
        self.question_bank.remove(self.question_dict)
        if self.question_bank:
            self.question_dict = random.choice(self.question_bank)
            self.question = self.question_dict["question"]
            self.correct_answer = self.question_dict["answer"]
            self.canvas.itemconfig(self.question_text, text=f"{self.question}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score is {self.score}")
            self.button1["state"] = DISABLED
            self.button2["state"] = DISABLED
            self.high_score()
            self.screen.quit()

    def high_score(self):
        try:
            with open(file="high_score.txt", mode='r') as score_file:
                self.hs = int(score_file.read())
        except FileNotFoundError:
            score_file = open(file="high_score.txt", mode='w')
            score_file.write(f"{self.hs}")
            score_file.close()
        if self.hs < self.score:
            self.hs = self.score
            with open(file="high_score.txt", mode='w') as score_file:
                score_file.write(f"{self.hs}")
            self.high_score_label.config(text=f"High Score: {self.hs}")

    def quit(self):
        self.screen.destroy()
