"""Shared result type for both search algorithms.

Kept separate from minimax.py/alphabeta.py so tests and the benchmark
script can import just this, and so both algorithms report stats in
exactly the same shape — that symmetry is what makes the M3/M5
comparisons meaningful.
"""

from dataclasses import dataclass


@dataclass
class SearchStats:
    nodes_visited: int = 0
    nodes_pruned: int = 0  # alpha-beta only; stays 0 for plain minimax
    depth_reached: int = 0
    time_seconds: float = 0.0
