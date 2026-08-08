from connect4.board import Board, Player
from connect4.connect4_board import Connect4Board, ROWS, COLS


def evaluate(board: Board, perspective: Player) -> float:
    """Score the board from `perspective`'s point of view. Higher = better."""
    assert isinstance(board, Connect4Board)
    grid = board._grid
    opponent = perspective.other

    score = 0.0

    # centre column control — pieces here participate in the most possible lines
    centre_col = COLS // 2
    centre_pieces = sum(1 for row in range(ROWS) if grid[row][centre_col] == perspective)
    score += centre_pieces * 3

    # score every window of 4 cells in all directions
    windows = _all_windows(grid)
    for window in windows:
        score += _score_window(window, perspective, opponent)

    return score


def _score_window(window: list, player: Player, opponent: Player) -> float:
    mine = window.count(player)
    theirs = window.count(opponent)
    empty = window.count(None)

    # window blocked by opponent — no value to us
    if theirs > 0 and mine > 0:
        return 0.0

    if mine == 4:
        return 100.0
    if mine == 3 and empty == 1:
        return 5.0
    if mine == 2 and empty == 2:
        return 2.0
    if theirs == 3 and empty == 1:
        return -4.0   # urgently block opponent's three-in-a-row
    return 0.0


def _all_windows(grid: list) -> list:
    windows = []

    # horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            windows.append([grid[row][col + i] for i in range(4)])

    # vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            windows.append([grid[row + i][col] for i in range(4)])

    # diagonal down-right
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            windows.append([grid[row + i][col + i] for i in range(4)])

    # diagonal down-left
    for row in range(ROWS - 3):
        for col in range(3, COLS):
            windows.append([grid[row + i][col - i] for i in range(4)])

    return windows