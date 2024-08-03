from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(pady=20, row=2, column=1, columnspan=2)
        self.question_text = self.canvas.create_text(150, 125,width=280, text=" ", font=("", 15, " "))
        self.score = Label(text=f"Score: ", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score.grid(row=1, column=2)
        check = self.photo = PhotoImage(file=r'E:\100 Days of python\day_34_quizzler\images\true.png')
        cross = self.photo = PhotoImage(file=r'E:\100 Days of python\day_34_quizzler\images\false.png')
        self.button_1 = Button(image=check, command = self.true_pressed )
        self.button_2 = Button(image=cross, command = self.false_pressed )
        self.button_1.grid(row=3, column=1)
        self.button_2.grid(row=3, column=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "END OF QUIZ.")
            self.button_1.config(state='disabled')
            self.button_2.config(state='disabled')

    def true_pressed(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)



