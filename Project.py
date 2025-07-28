from tkinter import *

# 🧠 Quiz Data
Questions = (
    "The set of all a belongs to R for which the equation x|x-1|+|x+2|+ a = 0 has exactly one real root, is",
    "Let m be a root of the equation 1 + x^2 + x^4 = 0. Then, the value of m^1011 + m^2023 - m^3033 is equal to",
    "A fair die is thrown until 2 appears. The probability that 2 appears on an even number of throws is",
    "A mass m is moving with a constant velocity along a line parallel to the x-axis, away from the origin. Its angular momentum with respect to the origin",
    "Who said that fluids, such as water, give an opposing force to a body called buoyant force?"
)

options = (
    ("A. (-∞, ∞)", "B. (-6, -3)", "C. (-6, ∞)", "D. (-∞, -3)"),
    ("A. 1", "B. m", "C. 1 + m", "D. 1 + 2m"),
    ("A. 5/11", "B. 1/6", "C. 5/6", "D. 6/11"),
    ("A. Is zero", "B. Remains constant", "C. Goes on increasing", "D. Goes on decreasing"),
    ("A. Newton", "B. Isaac Newton", "C. Archimedes", "D. C.V. Raman")
)

answers = ("A", "A", "A", "B", "C")

# 🎮 Variables
guesses = []
score = 0
question_num = 0

# 🪟 Window Setup
Window = Tk()
Window.title("Quiz Game")
Window.geometry("600x400")
Window.configure(bg="lightblue")

# 🎉 Welcome Message
welcome_label = Label(Window, text="Welcome to the Quiz!", font=('Arial', 20, 'bold'), bg='lightblue')
welcome_label.pack(pady=30)

start_button = Button(Window, text="Start Quiz", font=('Arial', 16, 'bold'), bg='white', command=lambda: start_quiz())
start_button.pack()

# 📋 Quiz Frame (initially hidden)
quiz_frame = Frame(Window, bg="lightyellow")
quiz_frame.pack(fill=BOTH, expand=True)
quiz_frame.pack_forget()

question_label = Label(quiz_frame, text="", font=('Arial', 14), wraplength=500, bg="lightyellow")
question_label.pack(pady=20)

guess = StringVar()
radio_buttons = []

for i in range(4):
    rb = Radiobutton(quiz_frame, text="", variable=guess, value="", font=("Arial", 12), bg="lightyellow", anchor="w")
    rb.pack(fill="x", padx=100, pady=2)
    radio_buttons.append(rb)

next_button = Button(quiz_frame, text="Next", font=('Arial', 12, 'bold'), command=lambda: next_question())
next_button.pack(pady=20)

result_label = Label(quiz_frame, text="", font=("Arial", 13), bg="lightyellow")
result_label.pack(pady=20)

# 🟡 Start Quiz Function
def start_quiz():
    welcome_label.pack_forget()
    start_button.pack_forget()
    quiz_frame.pack(fill=BOTH, expand=True)
    load_question()

# 📌 Load Next Question
def load_question():
    question_label.config(text=Questions[question_num])
    guess.set(None)
    for i in range(4):
        text = options[question_num][i]
        value = text[0]  # 'A', 'B', etc.
        radio_buttons[i].config(text=text, value=value)

# 🧪 Evaluate Answer & Progress
def next_question():
    global question_num, score

    selected = guess.get()
    if selected:
        guesses.append(selected)
        if selected == answers[question_num]:
            score += 1

        question_num += 1
        if question_num < len(Questions):
            load_question()
        else:
            show_result()
    else:
        result_label.config(text="⚠️ Please select an option before continuing.")

# 🏁 Final Result
def show_result():
    question_label.pack_forget()
    next_button.pack_forget()
    for rb in radio_buttons:
        rb.pack_forget()

    percentage = int((score / len(Questions)) * 100)
    result_text = "✅ Quiz Completed!\n\n"
    result_text += f"Your Score: {score} / {len(Questions)}\n"
    result_text += f"Score Percentage: {percentage}%\n"
    result_text += "Correct Answers: " + " ".join(answers) + "\n"
    result_text += "Your Guesses: " + " ".join(guesses)

    result_label.config(text=result_text)

# ▶️ Run
Window.mainloop()




        