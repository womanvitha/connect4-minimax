"""Plain minimax, no pruning.

MILESTONE M2 — implement this first, before alpha-beta. It's the
baseline: M3's alpha-beta must return the SAME move as this on every
test fixture, just by visiting fewer nodes. Get this right and correct
first; alpha-beta is this function plus two extra lines of bookkeeping.

Reminder of the recursion (see the worked example in chat for a traced
version of this on a toy tree):
    minimax(board, depth, maximizing_player)
      if depth == 0 or board.is_terminal(): return evaluate(board)
      if maximizing_player:
          return max(minimax(child, depth-1, False) for child in children)
      else:
          return min(minimax(child, depth-1, True) for child in children)
"""

from connect4.board import Board, Player
from connect4.evaluate import evaluate
from connect4.agent.stats import SearchStats


def minimax(
    board: Board,
    depth: int,
    maximizing_player: Player,
    stats: SearchStats,
) -> float:
    """Return the minimax value of `board` looking `depth` plies ahead.

    `maximizing_player` is fixed for the whole search (the player the
    agent is choosing a move for) — NOT the same as board.current_player(),
    which flips every ply.
    """
    stats.nodes_visited += 1

    # TODO(M2): base case — terminal position or depth exhausted
    #   terminal win/loss should return +inf / -inf (from maximizing_player's
    #   perspective), a draw returns 0, and depth==0 non-terminal calls evaluate()

    # TODO(M2): recursive case — current_player() tells you whether THIS
    # node is a max node or a min node; maximizing_player tells you who
    # the +inf/-inf should favour at the leaves

    raise NotImplementedError


def choose_move_minimax(board: Board, depth: int) -> tuple:
    """Top-level entry point: try every legal move, keep the best one.

    Returns (best_move, SearchStats).
    """
    # TODO(M2): for each move in board.valid_moves(), call minimax() on
    # the resulting child board and keep whichever move has the best
    # value from board.current_player()'s perspective
    raise NotImplementedError
