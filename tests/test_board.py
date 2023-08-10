import pytest
from cgol.board import Board


@pytest.fixture
def small_board():
    return Board(height=3, width=4)


@pytest.fixture
def first_generation():
    board = Board(height=10, width=10)
    board.set(1, 1, True)
    board.set(2, 1, True)
    board.set(3, 1, True)
    return board


@pytest.fixture
def second_generation():
    board = Board(height=10, width=10)
    board.set(2, 0, True)
    board.set(2, 1, True)
    board.set(2, 2, True)
    return board


def test_board_has_all_cells(small_board):
    assert (0, 0) in small_board.cells
    assert (0, 1) in small_board.cells
    assert (0, 2) in small_board.cells
    assert (1, 0) in small_board.cells
    assert (1, 1) in small_board.cells
    assert (1, 2) in small_board.cells
    assert (2, 0) in small_board.cells
    assert (2, 1) in small_board.cells
    assert (2, 2) in small_board.cells
    assert (3, 0) in small_board.cells
    assert (3, 1) in small_board.cells
    assert (3, 2) in small_board.cells


def test_board_does_not_go_out_of_bounds(small_board):
    assert (0, -1) not in small_board.cells
    assert (-1, 0) not in small_board.cells
    assert (-1, -1) not in small_board.cells
    assert (4, 2) not in small_board.cells
    assert (4, 3) not in small_board.cells


def test_neighbors_middle(small_board):
    coords = (1, 1)
    #            UL      U      UR       L       R       DL      D       DR
    expected = ((0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2))
    assert small_board.get_neighbors(coords[0], coords[1]) == expected


def test_neighbors_top_left(small_board):
    coords = (0, 0)
    # 3H 4W
    #            UL      U      UR       L       R       DL      D       DR
    expected = ((3, 2), (0, 2), (1, 2), (3, 0), (1, 0), (3, 1), (0, 1), (1, 1))
    assert small_board.get_neighbors(coords[0], coords[1]) == expected


def test_neighbors_top_right(small_board):
    coords = (3, 0)
    # 3H 4W
    #            UL      U      UR       L       R       DL      D       DR
    expected = ((2, 2), (3, 2), (0, 2), (2, 0), (0, 0), (2, 1), (3, 1), (0, 1))
    assert small_board.get_neighbors(coords[0], coords[1]) == expected


def test_neighbors_bottom_left(small_board):
    coords = (0, 2)
    # 3H 4W
    #            UL      U      UR       L       R       DL      D       DR
    expected = ((3, 1), (0, 1), (1, 1), (3, 2), (1, 2), (3, 0), (0, 0), (1, 0))
    assert small_board.get_neighbors(coords[0], coords[1]) == expected


def test_neighbors_bottom_right(small_board):
    coords = (3, 2)
    # 3H 4W
    #            UL      U      UR       L       R       DL      D       DR
    expected = ((2, 1), (3, 1), (0, 1), (2, 2), (0, 2), (2, 0), (3, 0), (0, 0))
    assert small_board.get_neighbors(coords[0], coords[1]) == expected


def test_get_set(small_board):
    small_board.set(0, 0, True)
    assert small_board.get(0, 0) == True


def test_validate_cell(small_board):
    assert small_board.validate_cell(-1, 0) is False
    assert small_board.validate_cell(0, -1) is False
    assert small_board.validate_cell(4, 0) is False
    assert small_board.validate_cell(0, 4) is False
    assert small_board.validate_cell(0, 0) is True
    assert small_board.validate_cell(3, 0) is True
    assert small_board.validate_cell(0, 2) is True
    assert small_board.validate_cell(3, 2) is True


def test_count_living_neighbors(first_generation):
    assert first_generation.count_living_neighbors(0, 0) == 1
    assert first_generation.count_living_neighbors(2, 0) == 3
    assert first_generation.count_living_neighbors(8, 8) == 0


def test_next_generation(first_generation, second_generation):
    expected = second_generation.cells
    actual = first_generation.get_next_generation()
    assert actual.cells == expected
    expected = first_generation.cells
    actual = second_generation.get_next_generation()
    assert actual.cells == expected
