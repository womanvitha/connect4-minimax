"""M3 spec.

The whole point of this file: alpha-beta must be a pure speed
optimisation, never a behaviour change. Every test here should compare
choose_move_alphabeta() against choose_move_minimax() on the SAME
fixture, not check alpha-beta's move against a hardcoded "correct"
answer — that keeps the two files honest against each other rather
than against your (possibly wrong) intuition about the position.
"""

import pytest

from connect4.connect4_board import Connect4Board
from connect4.agent.minimax import choose_move_minimax
from connect4.agent.alphabeta import choose_move_alphabeta

pytestmark = pytest.mark.skip(
    reason="M3: implement minimax (M2) and alpha-beta first"
)


@pytest.mark.parametrize("depth", [2, 3, 4, 5])
def test_same_move_as_plain_minimax(depth):
    board = Connect4Board()
    move_mm, _ = choose_move_minimax(board, depth)
    move_ab, _ = choose_move_alphabeta(board, depth)
    assert move_mm == move_ab


@pytest.mark.parametrize("depth", [3, 4, 5])
def test_visits_fewer_nodes_than_plain_minimax(depth):
    board = Connect4Board()
    _, stats_mm = choose_move_minimax(board, depth)
    _, stats_ab = choose_move_alphabeta(board, depth)
    assert stats_ab.nodes_visited < stats_mm.nodes_visited


def test_pruned_count_is_recorded():
    board = Connect4Board()
    _, stats_ab = choose_move_alphabeta(board, depth=4)
    assert stats_ab.nodes_pruned > 0
