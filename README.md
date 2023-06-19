# Conway's Game of Life
## A simple implementation of Conway's Game of Life with Pygame

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970 It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

Source: [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Rules

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Installation

1. Clone the repository

```bash
git clone https://github.com/W1L7dev/GameOfLife.git
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the program

```bash
python src/main.py
```