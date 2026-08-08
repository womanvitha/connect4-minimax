"""M2 spec.

The most useful fixtures here are small, hand-checkable positions where
you can work out the "obviously correct" move on paper (e.g. a board
one move away from a win, or one move away from letting the opponent
win) and assert the agent finds it. Resist the urge to only test the
opening position — an untested agent that "seems to play fine" is
exactly how subtle minimax bugs (off-by-one depth, wrong player
perspective at the leaves) survive into M3.
"""

import pytest

from connect4.connect4_board import Connect4Board
from connect4.agent.minimax import choose_move_minimax



def test_takes_immediate_winning_move():
    # TODO: set up a board where one column completes four-in-a-row
    # immediately, and assert choose_move_minimax picks that column
    # even at depth=1
    pass


def test_blocks_opponent_immediate_win():
    # TODO: set up a board where the opponent wins next turn unless
    # blocked, and assert the agent blocks at depth>=2
    pass


def test_node_count_grows_with_depth():
    board = Connect4Board()
    _, stats_shallow = choose_move_minimax(board, depth=2)
    _, stats_deep = choose_move_minimax(board, depth=4)
    assert stats_deep.nodes_visited > stats_shallow.nodes_visited
