"""Unified entry point the CLI (M4) and web UI (M6) will actually call.

Keeping this thin wrapper separate from minimax.py/alphabeta.py means
the UI code never needs to know which algorithm is running underneath
— useful later if you add a "compare both" mode for the node-count
benchmark (M5) without touching the UI at all.
"""

from connect4.board import Board
from connect4.agent.stats import SearchStats
from connect4.agent.minimax import choose_move_minimax
from connect4.agent.alphabeta import choose_move_alphabeta


def choose_move(board: Board, depth: int, use_alpha_beta: bool = True) -> tuple:
    """Pick a move for board.current_player().

    Returns (move, SearchStats). `depth` doubles as the difficulty
    setting exposed in the UI — deeper search = stronger, slower play.
    """
    if use_alpha_beta:
        return choose_move_alphabeta(board, depth)
    return choose_move_minimax(board, depth)
