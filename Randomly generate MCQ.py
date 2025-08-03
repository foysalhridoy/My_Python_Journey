import tkinter as tk
from tkinter import messagebox
import requests
import json

class TrueFalseGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 True / False Quiz Game")
        self.root.geometry("500x350")
        self.root.configure(bg="#e0f7fa")
        
        self.current_question = 0
        self.score = 0
        self.questions = []
        
        # Heading
        self.title_label = tk.Label(root, text="🧠 True / False Quiz", font=("Helvetica", 18, "bold"),
                                    bg="#e0f7fa", fg="#00796b")
        self.title_label.pack(pady=20)

        # Question Display
        self.question_label = tk.Label(root, text="Loading questions...", font=("Arial", 14), bg="white", 
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
        
        # Difficulty selection
        self.difficulty_var = tk.StringVar(value="medium")
        difficulty_frame = tk.Frame(root, bg="#e0f7fa")
        difficulty_frame.pack()
        
        tk.Label(difficulty_frame, text="Difficulty:", bg="#e0f7fa").pack(side=tk.LEFT)
        tk.Radiobutton(difficulty_frame, text="Easy", variable=self.difficulty_var, value="easy", bg="#e0f7fa").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(difficulty_frame, text="Medium", variable=self.difficulty_var, value="medium", bg="#e0f7fa").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(difficulty_frame, text="Hard", variable=self.difficulty_var, value="hard", bg="#e0f7fa").pack(side=tk.LEFT, padx=5)
        
        # Start button
        self.start_button = tk.Button(root, text="Start Quiz", font=("Arial", 12), 
                                     bg="#00796b", fg="white", command=self.fetch_questions, cursor="hand2")
        self.start_button.pack(pady=10)
        
        # Initially disable quiz buttons
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def fetch_questions(self):
        try:
            difficulty = self.difficulty_var.get()
            url = f"https://opentdb.com/api.php?amount=10&category=21&difficulty=hard&type=multiple"
            response = requests.get(url)
            data = response.json()
            
            if data["response_code"] == 0:
                self.questions = []
                for item in data["results"]:
                    # Decode HTML entities in questions
                    question = item["question"]
                    question = question.replace("&quot;", "'").replace("&#039;", "'")
                    self.questions.append({
                        "question": question,
                        "answer": item["correct_answer"] == "True"
                    })
                
                self.current_question = 0
                self.score = 0
                self.score_label.config(text="Score: 0")
                self.true_button.config(state="normal")
                self.false_button.config(state="normal")
                self.start_button.config(state="disabled")
                self.show_question()
            else:
                messagebox.showerror("Error", "Failed to fetch questions. Please try again.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def show_question(self):
        if self.current_question < len(self.questions):
            q_text = self.questions[self.current_question]["question"]
            self.question_label.config(text=q_text)
        else:
            self.end_quiz()

    def check_answer(self, user_answer):
        correct = self.questions[self.current_question]["answer"]
        if user_answer == correct:
            self.score += 1
        self.current_question += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.show_question()

    def end_quiz(self):
        self.question_label.config(text="🎉 Quiz Finished!")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.start_button.config(state="normal")
        messagebox.showinfo("Quiz Over", f"Your Final Score: {self.score}/{len(self.questions)}")

# === Run the Game ===
root = tk.Tk()
game = TrueFalseGame(root)
root.mainloop()
