import tkinter as tk
import random
# --------------------
# Game Setup
# --------------------
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
BALL_SIZE = 20
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
PADDLE_Y_OFFSET = 40
BALL_SPEED = 5

# --------------------
# Main Game Class
# --------------------
class CatchTheBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Catch the Ball Game")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()

        self.score = 0
        self.game_over = False

        # Create Paddle
        self.paddle = self.canvas.create_rectangle(160, WINDOW_HEIGHT - PADDLE_Y_OFFSET,
                                                   160 + PADDLE_WIDTH, WINDOW_HEIGHT - PADDLE_Y_OFFSET + PADDLE_HEIGHT,
                                                   fill="blue")

        # Create Ball
        self.ball = self.canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, fill="red")
        self.reset_ball()

        # Score Text
        self.score_text = self.canvas.create_text(10, 10, anchor='nw', fill='white',
                                                  font=('Arial', 14), text="Score: 0")

        # Bind movement
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.update()

    def reset_ball(self):
        self.ball_x = random.randint(0, WINDOW_WIDTH - BALL_SIZE)
        self.ball_y = 0

    def move_left(self, event):
        if not self.game_over:
            self.canvas.move(self.paddle, -20, 0)

    def move_right(self, event):
        if not self.game_over:
            self.canvas.move(self.paddle, 20, 0)

    def update(self):
        if self.game_over:
            return

        self.ball_y += BALL_SPEED
        self.canvas.coords(self.ball, self.ball_x, self.ball_y,
                           self.ball_x + BALL_SIZE, self.ball_y + BALL_SIZE)

        # Paddle Position
        paddle_coords = self.canvas.coords(self.paddle)

        # Ball hit bottom
        if self.ball_y + BALL_SIZE >= WINDOW_HEIGHT - PADDLE_Y_OFFSET:
            if paddle_coords[0] <= self.ball_x + BALL_SIZE / 2 <= paddle_coords[2]:
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                self.reset_ball()
            else:
                self.canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, fill="white",
                                        font=('Arial', 24), text="Game Over")
                self.game_over = True
                return

        self.root.after(30, self.update)

# --------------------
# Run the Game
# --------------------
if __name__ == "__main__":
    root = tk.Tk()
    game = CatchTheBallGame(root)
    root.mainloop()
