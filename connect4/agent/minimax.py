import math
import time
from connect4.board import Board, Player
from connect4.evaluate import evaluate
from connect4.agent.stats import SearchStats


def minimax(board: Board, depth: int, maximizing_player: Player, stats: SearchStats) -> float:
    stats.nodes_visited += 1

    if board.is_terminal():
        winner = board.winner()
        if winner == maximizing_player:
            return math.inf
        elif winner is not None:
            return -math.inf
        else:
            return 0.0

    if depth == 0:
        return evaluate(board, maximizing_player)

    if board.current_player() == maximizing_player:
        best = -math.inf
        for move in board.valid_moves():
            child = board.apply_move(move)
            best = max(best, minimax(child, depth - 1, maximizing_player, stats))
        return best
    else:
        best = math.inf
        for move in board.valid_moves():
            child = board.apply_move(move)
            best = min(best, minimax(child, depth - 1, maximizing_player, stats))
        return best


def choose_move_minimax(board: Board, depth: int) -> tuple:
    stats = SearchStats(depth_reached=depth)
    start = time.time()
    maximizing_player = board.current_player()
    best_move = None
    best_value = -math.inf

    for move in board.valid_moves():
        child = board.apply_move(move)
        value = minimax(child, depth - 1, maximizing_player, stats)
        if value > best_value:
            best_value = value
            best_move = move

    stats.time_seconds = time.time() - start
    return best_move, stats