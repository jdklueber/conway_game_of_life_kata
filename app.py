import random
from time import sleep
from cgol.board import Board

HEIGHT = 20
WIDTH = 30


board = Board(height=HEIGHT, width=WIDTH)
for x in range(WIDTH):
    for y in range(HEIGHT):
        board.set(x, y, bool(random.getrandbits(1)))


running = True
gen = 0

while running:
    sleep(0.2)
    gen += 1
    print(board)
    next_board = board.get_next_generation()

    if next_board.cells == board.cells:
        running = False
    board = next_board

print(f"Stagnation reached after {gen} generations.")
