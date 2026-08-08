from __future__ import annotations
from typing import Optional
import copy

from connect4.board import Board, Player

ROWS = 6
COLS = 7
CONNECT_N = 4


class Connect4Board(Board):

    def __init__(self, grid=None, to_move: Player = Player.ONE):
        if grid is None:
            self._grid = [[None] * COLS for _ in range(ROWS)]
        else:
            self._grid = grid
        self._to_move = to_move

    def valid_moves(self) -> list[int]:
        return [col for col in range(COLS) if self._grid[0][col] is None]

    def apply_move(self, move: int) -> Connect4Board:
        if move not in self.valid_moves():
            raise ValueError(f"Invalid move: column {move}")
        new_grid = copy.deepcopy(self._grid)
        for row in range(ROWS - 1, -1, -1):
            if new_grid[row][move] is None:
                new_grid[row][move] = self._to_move
                break
        return Connect4Board(new_grid, self._to_move.other)

    def is_terminal(self) -> bool:
        return self.winner() is not None or len(self.valid_moves()) == 0

    def winner(self) -> Optional[Player]:
        for player in [Player.ONE, Player.TWO]:
            if self._check_win(player):
                return player
        return None

    def current_player(self) -> Player:
        return self._to_move

    def clone(self) -> Connect4Board:
        return Connect4Board(copy.deepcopy(self._grid), self._to_move)

    def _check_win(self, player: Player) -> bool:
        # horizontal
        for row in range(ROWS):
            for col in range(COLS - 3):
                if all(self._grid[row][col + i] == player for i in range(4)):
                    return True
        # vertical
        for row in range(ROWS - 3):
            for col in range(COLS):
                if all(self._grid[row + i][col] == player for i in range(4)):
                    return True
        # diagonal down-right
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if all(self._grid[row + i][col + i] == player for i in range(4)):
                    return True
        # diagonal down-left
        for row in range(ROWS - 3):
            for col in range(3, COLS):
                if all(self._grid[row + i][col - i] == player for i in range(4)):
                    return True
        return False

    def __repr__(self) -> str:
        symbols = {None: ".", Player.ONE: "X", Player.TWO: "O"}
        rows = ["  ".join(symbols[cell] for cell in row) for row in self._grid]
        col_nums = "  ".join(str(c) for c in range(COLS))
        return "\n".join(rows) + "\n" + col_nums