![CI](https://github.com/womanvitha/connect4-minimax/actions/workflows/ci.yml/badge.svg)

# Connect 4 — Minimax AI with Alpha-Beta Pruning

A Connect 4 opponent built from AI coursework, playable in the browser.
The AI uses minimax search with alpha-beta pruning and an adjustable search
depth (difficulty). The stats bar shows live node counts after every AI move,
making the pruning optimisation visible as you play.

**[Play it live](https://womanvitha.github.io/connect4-minimax)**

---

## How it works

Minimax explores the game tree of possible future positions, assuming both
players play optimally. It scores terminal positions as win/loss/draw, and
non-terminal positions using a heuristic that rewards centre-column control
and open lines of 2 and 3 pieces.

Alpha-beta pruning cuts branches that cannot affect the final decision —
if a position is already known to be worse than a previously explored option,
the search stops early. This produces the identical move as plain minimax,
but visits significantly fewer nodes.

## Node-count savings (from the opening position)

| Depth | Minimax nodes | Alpha-beta nodes | Nodes saved | Saving |
|------:|-------------:|-----------------:|------------:|-------:|
|     3 |           399 |              296 |         103 |  25.8% |
|     4 |         2,800 |            1,227 |       1,573 |  56.2% |
|     5 |        19,607 |            6,557 |      13,050 |  66.6% |
|     6 |       137,256 |           24,764 |     112,492 |  82.0% |

At depth 6, alpha-beta visits 82% fewer nodes while making the same move.
Deeper search means stronger play — this is what makes the "Hard" difficulty
actually hard.

## Tech stack

- **Core + tests:** Python (stdlib only), pytest
- **Search:** minimax + alpha-beta pruning, adjustable depth
- **Evaluation:** centre-column control + open window scoring
- **Frontend:** Pyodide (Python compiled to WebAssembly — the same Python
  package runs directly in your browser, no backend required)
- **Deployment:** GitHub Pages (static, free, zero cold starts)

## Project structure

connect4/ core package
board.py abstract Board interface (game-agnostic)
connect4_board.py Connect 4 rules + win detection
evaluate.py heuristic position evaluation
agent/
minimax.py plain minimax + node counter
alphabeta.py minimax + alpha-beta pruning + node counter
agent.py unified choose_move() interface
tests/ pytest suite (M1–M5)
benchmarks/ node-count comparison script
cli/ terminal version
docs/ Pyodide browser frontend

## Running locally

```bash
pip install -e ".[dev]"
pytest -v
python -m cli.play_cli
python -m benchmarks.compare_nodes
```

## Milestones

- [x] M1 — Board & rules engine (Connect 4), full test coverage
- [x] M2 — Plain minimax agent + node counter
- [x] M3 — Alpha-beta pruning, proven equivalent to M2's move choice
- [x] M4 — Playable terminal (CLI) version
- [x] M5 — Position evaluation heuristic + node-count benchmark
- [x] M6 — Browser UI (Pyodide), deployed on GitHub Pages
- [x] M7 — README, CI badge

## Roadmap

- Othello as a second `Board` implementation, reusing the same agents
- Move ordering (centre-column-first) to improve pruning further
- Iterative deepening with a time budget instead of fixed depth

## Background

Built as a second-year portfolio project from AI coursework covering
minimax, alpha-beta pruning, and CSP backtracking.