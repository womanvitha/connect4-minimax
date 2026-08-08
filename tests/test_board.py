"""M1 spec: fill these in as Connect4Board.* methods are implemented,
and delete the skip markers one by one. Treat this file as the
definition of "done" for M1 — every case here should be a genuine
edge case, not a rewrite of the same happy path.
"""

import pytest

from connect4.board import Player
from connect4.connect4_board import Connect4Board



def test_empty_board_has_seven_valid_moves():
    board = Connect4Board()
    assert board.valid_moves() == list(range(7))


def test_full_column_is_not_a_valid_move():
    board = Connect4Board()
    for _ in range(6):  # fill column 0 to the top
        board = board.apply_move(0)
    assert 0 not in board.valid_moves()


def test_apply_move_does_not_mutate_original_board():
    board = Connect4Board()
    board.apply_move(3)
    assert board.valid_moves() == list(range(7))  # original untouched


@pytest.mark.parametrize(
    "moves",
    [
        [0, 1, 0, 1, 0, 1, 0],  # vertical: player ONE in column 0
    ],
)
def test_vertical_win(moves):
    board = Connect4Board()
    for move in moves:
        board = board.apply_move(move)
    assert board.is_terminal()
    assert board.winner() == Player.ONE


def test_horizontal_win():
    # TODO: pick 7 moves that give player ONE four-in-a-row horizontally
    pass


def test_diagonal_win_both_directions():
    # TODO: one fixture for "/" diagonal, one for "\" diagonal
    pass


def test_full_board_no_winner_is_a_draw():
    # TODO: a full 6x7 board with no four-in-a-row for either player
    pass


def test_illegal_move_raises():
    board = Connect4Board()
    with pytest.raises(ValueError):
        board.apply_move(99)
