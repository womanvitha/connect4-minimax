# Connect 4 AI — Minimax with Alpha-Beta Pruning

A Connect 4 opponent built from AI coursework (minimax, alpha-beta
pruning), playable in the browser, with an adjustable difficulty
(search depth) and a live comparison of alpha-beta vs plain minimax
node counts.

*Status: repo skeleton — see the milestone checklist below.*

<!-- Once M6 is done: live demo link + a short GIF of a game in progress -->

## Features (target)

- Play Connect 4 against a minimax + alpha-beta agent, in the browser
- Adjustable difficulty via search depth
- Node-count comparison: alpha-beta vs plain minimax, at each depth

## How it works

Minimax explores the game tree of possible future moves and assumes
both players play optimally; alpha-beta pruning skips branches that
are provably irrelevant to the final decision, without changing the
result. See `benchmarks/compare_nodes.py` for measured node-count
savings once M5 is done.

## Tech stack

- **Core + tests:** Python (stdlib only), pytest
- **Frontend:** Pyodide (the Python package runs directly in-browser
  via WebAssembly) + vanilla HTML/CSS/JS — no backend, deployed as a
  static site on GitHub Pages

## Project structure

```
connect4/            core package: board rules, evaluation, agents
  board.py             abstract Board interface (game-agnostic)
  connect4_board.py    Connect 4 rules
  evaluate.py          heuristic evaluation function
  agent/
    minimax.py           plain minimax + node counter
    alphabeta.py         minimax + alpha-beta pruning + node counter
    agent.py             unified choose_move() interface
tests/                pytest suite (mirrors the milestones below)
benchmarks/           node-count comparison script
cli/                  terminal play, for sanity-checking the agent
web/                  Pyodide-based browser frontend
```

## Running locally

```bash
pip install -e ".[dev]"
pytest -v                     # run the test suite
python -m cli.play_cli        # play against the AI in the terminal
python -m benchmarks.compare_nodes   # node-count comparison table
```

## Milestones

- [ ] M1 — Board & rules engine (Connect 4), full test coverage
- [ ] M2 — Plain minimax agent + node counter
- [ ] M3 — Alpha-beta pruning, proven equivalent to M2's move choice
- [ ] M4 — Playable terminal (CLI) version
- [ ] M5 — Node-count benchmark script
- [ ] M6 — Browser UI (Pyodide), deployed on GitHub Pages
- [ ] M7 — README polish, demo GIF, CI badge

## Roadmap / stretch goals

- Othello as a second `Board` implementation, reusing the same agents
- Move ordering (centre-column-first) to improve pruning further
- Iterative deepening with a time budget instead of a fixed depth

## Background

Built as a portfolio project from second-year AI coursework covering
minimax, alpha-beta pruning, and CSP backtracking.
