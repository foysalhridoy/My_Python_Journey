import tkinter as tk
import random

# Game settings
WIDTH = 600
HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30
ZOMBIE_SIZE = 30
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
PLAYER_SPEED = 20
ZOMBIE_SPEED = 2
BULLET_SPEED = 10

class ZombieShooterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🧟 Zombie Shooter: Defense Night")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1c1c1c")
        self.canvas.pack()

        self.score = 0
        self.health = 3
        self.ammo = 5
        self.game_over = False

        # Display HUD
        self.hud = {
            "score": self.canvas.create_text(10, 10, anchor='nw', fill='white', font=('Consolas', 14),
                                             text=f"Score: {self.score}"),
            "health": self.canvas.create_text(10, 30, anchor='nw', fill='red', font=('Consolas', 14),
                                              text=f"Health: {self.health}"),
            "ammo": self.canvas.create_text(10, 50, anchor='nw', fill='cyan', font=('Consolas', 14),
                                            text=f"Ammo: {self.ammo}")
        }

        # Player character
        self.player = self.canvas.create_rectangle(WIDTH//2 - PLAYER_WIDTH//2, HEIGHT - PLAYER_HEIGHT - 10,
                                                   WIDTH//2 + PLAYER_WIDTH//2, HEIGHT - 10,
                                                   fill="#00ffaa")

        self.bullets = []
        self.zombies = []

        # Controls
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)

        self.spawn_zombie()
        self.update()

    def move_left(self, event):
        if not self.game_over:
            self.canvas.move(self.player, -PLAYER_SPEED, 0)

    def move_right(self, event):
        if not self.game_over:
            self.canvas.move(self.player, PLAYER_SPEED, 0)

    def shoot(self, event):
        if self.game_over or self.ammo <= 0:
            return
        self.ammo -= 1
        self.update_hud()
        px1, py1, px2, py2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle((px1 + px2)//2 - BULLET_WIDTH//2, py1 - BULLET_HEIGHT,
                                              (px1 + px2)//2 + BULLET_WIDTH//2, py1,
                                              fill="yellow")
        self.bullets.append(bullet)

    def spawn_zombie(self):
        if not self.game_over:
            x = random.randint(0, WIDTH - ZOMBIE_SIZE)
            zombie = self.canvas.create_rectangle(x, 0, x + ZOMBIE_SIZE, ZOMBIE_SIZE,
                                                  fill="green")
            self.zombies.append(zombie)
            self.root.after(2000, self.spawn_zombie)

    def update(self):
        if self.game_over:
            return

        # Move bullets
        for bullet in self.bullets[:]:
            self.canvas.move(bullet, 0, -BULLET_SPEED)
            if self.canvas.coords(bullet)[1] <= 0:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)

        # Move zombies
        for zombie in self.zombies[:]:
            self.canvas.move(zombie, 0, ZOMBIE_SPEED)
            zx1, zy1, zx2, zy2 = self.canvas.coords(zombie)

            # Check bullet collision
            for bullet in self.bullets[:]:
                if self.check_collision(zombie, bullet):
                    self.canvas.delete(zombie)
                    self.canvas.delete(bullet)
                    self.zombies.remove(zombie)
                    self.bullets.remove(bullet)
                    self.score += 1
                    self.ammo += 1
                    self.update_hud()
                    break

            # Check if zombie touches player
            if zy2 >= HEIGHT - PLAYER_HEIGHT - 10:
                self.canvas.delete(zombie)
                self.zombies.remove(zombie)
                self.health -= 1
                self.update_hud()
                if self.health <= 0:
                    self.end_game()

        self.root.after(30, self.update)

    def update_hud(self):
        self.canvas.itemconfig(self.hud["score"], text=f"Score: {self.score}")
        self.canvas.itemconfig(self.hud["health"], text=f"Health: {self.health}")
        self.canvas.itemconfig(self.hud["ammo"], text=f"Ammo: {self.ammo}")

    def check_collision(self, obj1, obj2):
        x1, y1, x2, y2 = self.canvas.coords(obj1)
        a1, b1, a2, b2 = self.canvas.coords(obj2)
        return not (x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2)

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text="💀 GAME OVER",
                                fill="white", font=("Consolas", 28))


# Run Game
if __name__ == "__main__":
    root = tk.Tk()
    game = ZombieShooterGame(root)
    root.mainloop()
