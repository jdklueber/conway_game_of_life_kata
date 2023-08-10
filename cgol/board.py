class Board:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.cells: dict[tuple, bool] = {}
        for x in range(width):
            for y in range(height):
                self.cells[(x, y)] = False

    def get_neighbors(self, x: int, y: int) -> (int, int):
        upleft = ((x - 1) % self.width, (y - 1) % self.height)
        up = (x, (y - 1) % self.height)
        upright = ((x + 1) % self.width, (y - 1) % self.height)
        left = ((x - 1) % self.width, y)
        right = ((x + 1) % self.width, y)
        downleft = ((x - 1) % self.width, (y + 1) % self.height)
        down = (x, (y + 1) % self.height)
        downright = ((x + 1) % self.width, (y + 1) % self.height)

        return (upleft, up, upright, left, right, downleft, down, downright)

    def validate_cell(self, x: int, y: int):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def set(self, x: int, y: int, value: bool):
        if self.validate_cell(x, y):
            self.cells[(x, y)] = value
        else:
            raise ValueError(f"Cell {x, y} is out of bounds")

    def get(self, x: int, y: int) -> bool:
        if self.validate_cell(x, y):
            return self.cells[(x, y)]

        raise ValueError(f"Cell {x, y} is out of bounds")

    def count_living_neighbors(self, x, y):
        return len(
            [cell for cell in self.get_neighbors(x, y) if self.cells[cell] is True]
        )

    def get_next_generation(self):
        result = Board(height=self.height, width=self.width)
        for cell in self.cells.items():
            ((x, y), value) = cell
            living_neighbors = self.count_living_neighbors(x, y)
            if value is False and living_neighbors == 3:
                result.set(x, y, True)
            elif value is True and living_neighbors == 2 or living_neighbors == 3:
                result.set(x, y, True)
        return result

    def __str__(self):
        result = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                result += "O" if self.get(x, y) else "."
            result += "\n"
        return result
