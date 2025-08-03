import tkinter as tk
from tkinter import messagebox

# === Sample Questions ===
questions = [
    {"question": "Python is a programming language.", "answer": True},
    {"question": "Sun rises from the West.", "answer": False},
    {"question": "The Earth orbits the Sun.", "answer": True},
    {"question": "2 + 2 equals 5.", "answer": False},
    {"question": "Water freezes at 0°C.", "answer": True}
]

# === Main Class ===
class TrueFalseGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 True / False Quiz Game")
        self.root.geometry("500x350")
        self.root.configure(bg="#e0f7fa")
        
        self.current_question = 0
        self.score = 0

        # Heading
        self.title_label = tk.Label(root, text="🧠 True / False Quiz", font=("Helvetica", 18, "bold"),
                                    bg="#e0f7fa", fg="#00796b")
        self.title_label.pack(pady=20)

        # Question Display
        self.question_label = tk.Label(root, text="", font=("Arial", 14), bg="white", 
                                       wraplength=400, justify="center", relief="ridge", bd=3, padx=10, pady=10)
        self.question_label.pack(pady=20)

        # Buttons Frame
        button_frame = tk.Frame(root, bg="#e0f7fa")
        button_frame.pack()

        self.true_button = tk.Button(button_frame, text="✅ TRUE", width=12, font=("Arial", 12, "bold"),
                                     bg="#4caf50", fg="white", command=lambda: self.check_answer(True), cursor="hand2")
        self.true_button.grid(row=0, column=0, padx=10, pady=10)

        self.false_button = tk.Button(button_frame, text="❌ FALSE", width=12, font=("Arial", 12, "bold"),
                                      bg="#f44336", fg="white", command=lambda: self.check_answer(False), cursor="hand2")
        self.false_button.grid(row=0, column=1, padx=10, pady=10)

        # Score Label
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12), bg="#e0f7fa", fg="#004d40")
        self.score_label.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.current_question < len(questions):
            q_text = questions[self.current_question]["question"]
            self.question_label.config(text=q_text)
        else:
            self.end_quiz()

    def check_answer(self, user_answer):
        correct = questions[self.current_question]["answer"]
        if user_answer == correct:
            self.score += 1
        self.current_question += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.show_question()

    def end_quiz(self):
        self.question_label.config(text="🎉 Quiz Finished!")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        messagebox.showinfo("Quiz Over", f"Your Final Score: {self.score}/{len(questions)}")

# === Run the Game ===
root = tk.Tk()
game = TrueFalseGame(root)
root.mainloop()
