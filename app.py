from cgol.board import Board

board = Board(height=10, width=10)
board.set(1, 1, True)
board.set(2, 1, True)
board.set(3, 1, True)

running = True

while running:
    print(board)
    board = board.get_next_generation()
    choice = input("Next gen? (Y/n):   ")
    if choice == "n":
        running = False
