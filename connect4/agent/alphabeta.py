"""Minimax with alpha-beta pruning.

MILESTONE M3 — this is minimax.py plus two extra parameters (alpha,
beta) and one extra check. The worked example earlier in the chat
traces exactly this logic on a 9-leaf toy tree: a MIN node can stop
exploring its children the moment its running value drops to <= alpha
(its parent MAX already has a better guaranteed option elsewhere), and
symmetrically a MAX node stops once its value rises >= beta.

Correctness contract (see tests/test_alphabeta.py): for every fixture,
choose_move_alphabeta() must return the SAME move as
choose_move_minimax() from M2, while stats.nodes_visited is strictly
lower (for any fixture with a real pruning opportunity). If the moves
ever disagree, the bug is in this file, not in the test.
"""

from connect4.board import Board, Player
from connect4.evaluate import evaluate
from connect4.agent.stats import SearchStats

NEG_INF = float("-inf")
POS_INF = float("inf")


def alphabeta(
    board: Board,
    depth: int,
    alpha: float,
    beta: float,
    maximizing_player: Player,
    stats: SearchStats,
) -> float:
    """Same contract as minimax(), plus alpha/beta bounds.

    alpha: best value MAX can guarantee so far, on the path to this node.
    beta:  best value MIN can guarantee so far, on the path to this node.
    """
    stats.nodes_visited += 1

    # TODO(M3): base case — identical to minimax.py's base case

    # TODO(M3): recursive case — same structure as minimax.py, but:
    #   - at a MAX node: after each child, update alpha = max(alpha, value);
    #     if alpha >= beta, increment stats.nodes_pruned by the number of
    #     remaining unvisited children and stop (break) the loop
    #   - at a MIN node: symmetric, update beta = min(beta, value);
    #     if beta <= alpha, prune the remaining children and break

    raise NotImplementedError


def choose_move_alphabeta(board: Board, depth: int) -> tuple:
    """Top-level entry point, mirrors choose_move_minimax()."""
    # TODO(M3): same as choose_move_minimax(), but seed each top-level
    # call with alpha=NEG_INF, beta=POS_INF
    raise NotImplementedError
