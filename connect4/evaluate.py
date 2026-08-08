"""Heuristic evaluation for non-terminal positions at the search cutoff.

MILESTONE M2 (basic) / iterate later — this is the one file worth
revisiting after everything else works, since it's what makes the
agent look "smart" rather than random at shallow depths.

Suggested starting heuristic (score from Player.ONE's perspective,
negate for Player.TWO):
    + heavily reward actual wins / penalise losses (handled by the
      search itself returning +inf/-inf, not this function)
    + centre-column control (pieces near column 3 are more valuable —
      they participate in more possible lines of 4)
    + count of open 2-in-a-rows and 3-in-a-rows for each player,
      weighted (e.g. 3-in-a-row worth much more than 2-in-a-row)
"""

from connect4.board import Board, Player


def evaluate(board: Board, perspective: Player) -> float:
    """Static evaluation of `board` from `perspective`'s point of view.

    Higher is better for `perspective`. Only called on non-terminal
    boards at the depth cutoff — terminal wins/losses/draws are scored
    directly by the search functions in agent/.
    """
    # TODO(M2): replace with a real heuristic; this stub treats every
    # position as neutral, which will make the depth-limited agent play
    # essentially randomly until this is implemented.
    return 0.0
