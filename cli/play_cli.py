from connect4.connect4_board import Connect4Board
from connect4.board import Player
from connect4.agent.agent import choose_move


def play():
    print("Connect 4 — you are X (Player 1), AI is O (Player 2)")
    depth = input("AI search depth (1=easy, 4=medium, 6=hard): ").strip()
    depth = int(depth) if depth.isdigit() else 4

    board = Connect4Board()

    while not board.is_terminal():
        print("\n" + repr(board))

        if board.current_player() == Player.ONE:
            raw = input("Your move (0-6): ").strip()
            if not raw.isdigit() or int(raw) not in board.valid_moves():
                print(f"Invalid — choose from {board.valid_moves()}")
                continue
            board = board.apply_move(int(raw))
        else:
            print("AI thinking...")
            move, stats = choose_move(board, depth)
            print(f"AI plays column {move}  "
                  f"({stats.nodes_visited} nodes visited, "
                  f"{stats.nodes_pruned} pruned, "
                  f"{stats.time_seconds:.2f}s)")
            board = board.apply_move(move)

    print("\n" + repr(board))
    winner = board.winner()
    if winner == Player.ONE:
        print("You win!")
    elif winner == Player.TWO:
        print("AI wins!")
    else:
        print("Draw!")


if __name__ == "__main__":
    play()
    