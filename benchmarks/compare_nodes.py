from connect4.connect4_board import Connect4Board
from connect4.agent.minimax import choose_move_minimax
from connect4.agent.alphabeta import choose_move_alphabeta

DEPTHS = [2, 3, 4, 5, 6]


def run() -> None:
    board = Connect4Board()
    print(f"{'Depth':>5} | {'Minimax nodes':>14} | {'Alpha-beta nodes':>16} | {'Nodes saved':>11} | {'Saving':>7}")
    print("-" * 64)
    for depth in DEPTHS:
        _, stats_mm = choose_move_minimax(board, depth)
        _, stats_ab = choose_move_alphabeta(board, depth)
        saved = stats_mm.nodes_visited - stats_ab.nodes_visited
        saving_pct = saved / stats_mm.nodes_visited
        print(
            f"{depth:>5} | {stats_mm.nodes_visited:>14,} | "
            f"{stats_ab.nodes_visited:>16,} | "
            f"{saved:>11,} | {saving_pct:>7.1%}"
        )


if __name__ == "__main__":
    run()