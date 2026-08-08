"""M5 spec.

Guards the claim you'll put in the README ("alpha-beta visits N% fewer
nodes") against silently regressing — e.g. if a future move-ordering
change accidentally makes pruning worse rather than better.
"""

import pytest

from connect4.connect4_board import Connect4Board
from connect4.agent.minimax import choose_move_minimax
from connect4.agent.alphabeta import choose_move_alphabeta

pytestmark = pytest.mark.skip(reason="M5: implement M2 and M3 first")


@pytest.mark.parametrize("depth", [2, 3, 4, 5, 6])
def test_pruning_savings_are_positive_at_every_depth(depth):
    board = Connect4Board()
    _, stats_mm = choose_move_minimax(board, depth)
    _, stats_ab = choose_move_alphabeta(board, depth)
    savings = 1 - (stats_ab.nodes_visited / stats_mm.nodes_visited)
    assert savings > 0, f"no pruning benefit at depth {depth}"
