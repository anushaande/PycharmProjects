from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.true_btn = Button()
        true_image = PhotoImage(file="images/true.png")
        self.true_btn.config(image=true_image, highlightthickness=0, command=self.tru_btn_cmd)
        self.true_btn.grid(column=0, row=2)

        self.false_btn = Button()
        false_image = PhotoImage(file="images/false.png")
        self.false_btn.config(image=false_image, highlightthickness=0, command=self.false_btn_cmd)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text=f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz\n Your score: {self.quiz.score}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def tru_btn_cmd(self):
        user_answer = "True"
        self.give_feedback(user_answer)

    def false_btn_cmd(self):
        user_answer = "False"
        self.give_feedback(user_answer)

    def give_feedback(self, user_answer):
        is_correct = self.quiz.check_answer(user_answer)
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
