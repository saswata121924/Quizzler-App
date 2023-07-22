from ui import QuizScreen
from tkinter import messagebox

# Continue Playing the Quiz Game until the user decides to quit.
choice = True
while choice:
    call = QuizScreen()
    choice = messagebox.askyesno(title="Quizzler App", message="Do you want to play again?")
    call.quit()
