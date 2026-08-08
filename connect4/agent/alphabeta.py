import math
import time
from connect4.board import Board, Player
from connect4.evaluate import evaluate
from connect4.agent.stats import SearchStats


def alphabeta(board: Board, depth: int, alpha: float, beta: float,
              maximizing_player: Player, stats: SearchStats) -> float:
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

    moves = board.valid_moves()

    if board.current_player() == maximizing_player:
        best = -math.inf
        for move in moves:
            child = board.apply_move(move)
            best = max(best, alphabeta(child, depth - 1, alpha, beta, maximizing_player, stats))
            alpha = max(alpha, best)
            if alpha >= beta:
                stats.nodes_pruned += len(moves) - moves.index(move) - 1
                break
        return best
    else:
        best = math.inf
        for move in moves:
            child = board.apply_move(move)
            best = min(best, alphabeta(child, depth - 1, alpha, beta, maximizing_player, stats))
            beta = min(beta, best)
            if beta <= alpha:
                stats.nodes_pruned += len(moves) - moves.index(move) - 1
                break
        return best


def choose_move_alphabeta(board: Board, depth: int) -> tuple:
    stats = SearchStats(depth_reached=depth)
    start = time.time()
    maximizing_player = board.current_player()
    best_move = board.valid_moves()[0]
    best_value = -math.inf

    for move in board.valid_moves():
        child = board.apply_move(move)
        value = alphabeta(child, depth - 1, -math.inf, math.inf, maximizing_player, stats)
        if value > best_value:
            best_value = value
            best_move = move

    stats.time_seconds = time.time() - start
    return best_move, stats