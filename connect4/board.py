"""Game-agnostic board interface.

Both Connect 4 and Othello (added later) implement this ABC. Keeping the
interface here — rather than baking Connect 4 specifics into the agent —
is what lets minimax/alpha-beta code in agent/ be reused unchanged for a
second game.

Design decision: Board is treated as IMMUTABLE. apply_move() returns a
new Board rather than mutating self. This avoids undo-move bookkeeping
in the recursive search and makes positions safe to reuse/cache later
(e.g. a transposition table in a stretch milestone).
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Optional


class Player(Enum):
    ONE = 1
    TWO = 2

    @property
    def other(self) -> "Player":
        return Player.TWO if self is Player.ONE else Player.ONE


class Board(ABC):
    """Shared interface for any two-player, perfect-information,
    zero-sum board game playable by the minimax/alpha-beta agents.
    """

    @abstractmethod
    def valid_moves(self) -> list[Any]:
        """Legal moves from this position, for the current player."""
        raise NotImplementedError

    @abstractmethod
    def apply_move(self, move: Any) -> "Board":
        """Return a NEW Board after current_player() plays `move`.

        Must not mutate self. Raise ValueError on an illegal move.
        """
        raise NotImplementedError

    @abstractmethod
    def is_terminal(self) -> bool:
        """True if the game has ended (a player has won, or it's a draw)."""
        raise NotImplementedError

    @abstractmethod
    def winner(self) -> Optional[Player]:
        """The winning Player, or None if drawn / not yet finished."""
        raise NotImplementedError

    @abstractmethod
    def current_player(self) -> Player:
        """Whose turn it is to move."""
        raise NotImplementedError

    @abstractmethod
    def clone(self) -> "Board":
        """Deep copy — used in tests/debugging, not required in the hot path."""
        raise NotImplementedError
