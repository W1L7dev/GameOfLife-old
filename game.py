"""
CONWAY'S GAME OF LIFE
~~~~~~~~~~~~~~~~~~~~~
A simple implementation of Conway's Game of Life in Python.
Author: W1L7dev

RULES
~~~~~
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

import pygame
import numpy as np

class Values:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.PURPLE = (128, 0, 128)

        self.WIDTH, self.HEIGHT = 800, 800
        self.ROWS, self.COLS = 80, 80

        self.SQUARE_SIZE = self.WIDTH // self.ROWS

        self.TITLE = "Conway's Game of Life"
        self.FPS = 15
        self.WIN_SIZE = (self.WIDTH, self.HEIGHT)


class Grid(Values):
    def __init__(self):
        super().__init__()
        self.grid = np.zeros((self.ROWS, self.COLS))

    def draw_grid(self, win):
        for i in range(self.ROWS):
            pygame.draw.line(
                win,
                self.BLACK,
                (0, i * self.SQUARE_SIZE),
                (self.WIDTH, i * self.SQUARE_SIZE),
            )
            for j in range(self.COLS):
                pygame.draw.line(
                    win,
                    self.BLACK,
                    (j * self.SQUARE_SIZE, 0),
                    (j * self.SQUARE_SIZE, self.HEIGHT),
                )

    def draw_squares(self, win):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(
                        win,
                        self.WHITE,
                        (
                            j * self.SQUARE_SIZE,
                            i * self.SQUARE_SIZE,
                            self.SQUARE_SIZE,
                            self.SQUARE_SIZE,
                        ),
                    )

    def update_grid(self):
        new_grid = np.zeros((self.ROWS, self.COLS))
        for i in range(self.ROWS):
            for j in range(self.COLS):
                new_grid[i][j] = self.check_neighbors(i, j)
        self.grid = new_grid

    def check_neighbors(self, i, j):
        neighbors = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if i + x < 0 or j + y < 0 or i + x >= self.ROWS or j + y >= self.COLS:
                    continue
                if x == 0 and y == 0:
                    continue
                if self.grid[i + x][j + y] == 1:
                    neighbors += 1
        if self.grid[i][j] == 1 and neighbors < 2:
            return 0
        elif self.grid[i][j] == 1 and neighbors > 3:
            return 0
        elif self.grid[i][j] == 0 and neighbors == 3:
            return 1
        else:
            return self.grid[i][j]


class Button(Values):
    def __init__(self, x, y, w, h, text, color, behaviour):
        super().__init__()
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.text = text
        self.color = color
        self.behaviour = behaviour

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))
        font = pygame.font.SysFont("arial", 20)
        text = font.render(self.text, True, self.WHITE)
        win.blit(
            text,
            (
                self.x + self.w // 2 - text.get_width() // 2,
                self.y + self.h // 2 - text.get_height() // 2,
            ),
        )

    def clicked(self, pos):
        x, y = pos
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            return True
        return False


class Game(Grid):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.win = pygame.display.set_mode(self.WIN_SIZE)
        pygame.display.set_caption(self.TITLE)
        self.clock = pygame.time.Clock()
        self.run = True
        self.paused = True
        self.generation = 0

        self.buttons = [
            Button(10, 10, 100, 50, "Start", self.GREEN, self.start),
            Button(120, 10, 100, 50, "Pause", self.RED, self.pause),
            Button(230, 10, 100, 50, "Clear", self.BLUE, self.clear),
            Button(340, 10, 130, 50, "Randomize", self.PURPLE, self.random),
        ]

    def start(self):
        self.paused = False

    def pause(self):
        self.paused = True

    def clear(self):
        self.grid = np.zeros((self.ROWS, self.COLS))
        self.generation = 0

    def random(self):
        self.grid = np.random.randint(2, size=(self.ROWS, self.COLS))

    def run_game(self):
        while self.run:
            self.clock.tick(self.FPS)
            self.events()
            self.draw()
            if not self.paused:
                self.update_grid()
                self.update_generation()

    def draw_generation(self, win):
        font = pygame.font.SysFont("arial", 20)
        text = font.render(f"Generation: {self.generation}", True, self.GREEN)
        win.blit(text, (self.WIDTH - text.get_width() - 10, 10))

    def update_generation(self):
        self.generation += 1

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.clicked(pos):
                        button.behaviour()

    def draw(self):
        self.win.fill(self.BLACK)
        self.draw_grid(self.win)
        self.draw_squares(self.win)
        for button in self.buttons:
            button.draw(self.win)
        if not self.paused:
            self.update_grid()
            self.draw_generation(self.win)
        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run_game()
