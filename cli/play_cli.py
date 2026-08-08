"""MILESTONE M4.

Run with: python -m cli.play_cli

The cheapest possible way to confirm the whole M1-M3 stack actually
works end to end before investing time in a web UI. If this is
frustrating or buggy to play against, the web UI will be too.
"""

from connect4.connect4_board import Connect4Board
from connect4.agent.agent import choose_move


def print_board(board: Connect4Board) -> None:
    # TODO(M4): print a readable ASCII grid (e.g. using board.__repr__
    # once that's filled in, or directly here)
    print(board)


def play() -> None:
    board = Connect4Board()
    depth = int(input("AI search depth (try 4-6 to start): ") or 4)

    while not board.is_terminal():
        print_board(board)
        if board.current_player().value == 1:  # human is Player.ONE
            move = int(input(f"Your move {board.valid_moves()}: "))
            board = board.apply_move(move)
        else:
            move, stats = choose_move(board, depth)
            print(f"AI plays column {move} "
                  f"({stats.nodes_visited} nodes, {stats.nodes_pruned} pruned)")
            board = board.apply_move(move)

    print_board(board)
    winner = board.winner()
    print(f"Winner: {winner}" if winner else "Draw!")


if __name__ == "__main__":
    play()
