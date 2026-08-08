"""MILESTONE M5.

Run with: python -m benchmarks.compare_nodes

Produces a table (and optionally a matplotlib chart, saved to
benchmarks/output/) of nodes visited by plain minimax vs alpha-beta,
across a range of depths, on a fixed set of positions. This is the
data behind the "node-count savings" bonus feature and the README's
results table.
"""

from connect4.connect4_board import Connect4Board
from connect4.agent.minimax import choose_move_minimax
from connect4.agent.alphabeta import choose_move_alphabeta

DEPTHS = [1, 2, 3, 4, 5, 6, 7, 8]


def run() -> None:
    board = Connect4Board()
    print(f"{'depth':>5} | {'minimax nodes':>14} | {'alphabeta nodes':>16} | {'savings':>8}")
    print("-" * 54)
    for depth in DEPTHS:
        # TODO(M5): once M2/M3 are done, this loop just works
        _, stats_mm = choose_move_minimax(board, depth)
        _, stats_ab = choose_move_alphabeta(board, depth)
        savings = 1 - (stats_ab.nodes_visited / stats_mm.nodes_visited)
        print(
            f"{depth:>5} | {stats_mm.nodes_visited:>14} | "
            f"{stats_ab.nodes_visited:>16} | {savings:>7.1%}"
        )
    # TODO(M5, optional): also save a matplotlib bar/line chart to
    # benchmarks/output/nodes_by_depth.png for the README


if __name__ == "__main__":
    run()
