import random
from time import sleep
from cgol.board import Board

HEIGHT = 20
WIDTH = 30
MAX_HISTORY = 10

board = Board(height=HEIGHT, width=WIDTH)
for x in range(WIDTH):
    for y in range(HEIGHT):
        board.set(x, y, bool(random.getrandbits(1)))


running = True
gen = 0
history = []

while running:
    sleep(0.2)
    gen += 1
    print(board)
    next_board = board.get_next_generation()

    history.append(board.cells)
    board = next_board
    if len(history) > MAX_HISTORY:
        history.pop(0)

    if board.cells in history:
        running = False


print(f"Stagnation reached after {gen} generations.")
