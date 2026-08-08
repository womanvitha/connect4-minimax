const ROWS = 6, COLS = 7;
let pyodide = null;
let gameOver = false;
let playerTurn = true;

async function init() {
  setLoading("Loading Python runtime (first visit may take ~10s)...");
  pyodide = await loadPyodide();

  setLoading("Installing game engine...");
  await pyodide.loadPackage("micropip");
  const micropip = pyodide.pyimport("micropip");
  await micropip.install("./connect4_ai-0.1.0-py3-none-any.whl");

  await pyodide.runPythonAsync(`
from connect4.connect4_board import Connect4Board
from connect4.board import Player
from connect4.agent.agent import choose_move
import json

board = Connect4Board()

def get_grid():
    symbols = {None: 0}
    symbols[Player.ONE] = 1
    symbols[Player.TWO] = 2
    return json.dumps([[symbols[board._grid[r][c]] for c in range(7)] for r in range(6)])

def apply_human_move(col):
    global board
    board = board.apply_move(col)

def get_ai_move(depth):
    global board
    move, stats = choose_move(board, depth)
    board = board.apply_move(move)
    return json.dumps({
        "move": move,
        "nodes": stats.nodes_visited,
        "pruned": stats.nodes_pruned,
        "time": round(stats.time_seconds, 2)
    })

def is_terminal():
    return board.is_terminal()

def get_winner():
    w = board.winner()
    if w is None: return 0
    return 1 if w.value == 1 else 2

def reset():
    global board
    board = Connect4Board()

def valid_moves_list():
    return json.dumps(board.valid_moves())
  `);

  document.getElementById("loading").classList.add("hidden");
  document.getElementById("game").classList.remove("hidden");
  buildBoard();
  buildColButtons();
  document.getElementById("new-game-btn").addEventListener("click", newGame);
  setStatus("Your turn — click a column");
}

function buildBoard() {
  const board = document.getElementById("board");
  board.innerHTML = "";
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      const cell = document.createElement("div");
      cell.className = "cell";
      cell.id = `cell-${r}-${c}`;
      board.appendChild(cell);
    }
  }
}

function buildColButtons() {
  const wrap = document.getElementById("col-buttons");
  wrap.innerHTML = "";
  for (let c = 0; c < COLS; c++) {
    const btn = document.createElement("button");
    btn.className = "col-btn";
    btn.textContent = c;
    btn.addEventListener("click", () => humanMove(c));
    wrap.appendChild(btn);
  }
}

function setLoading(msg) {
  document.getElementById("loading-msg").textContent = msg;
}

function setStatus(msg) {
  document.getElementById("status").textContent = msg;
}

function setStats(msg) {
  const bar = document.getElementById("stats-bar");
  if (msg) {
    bar.classList.remove("hidden");
    document.getElementById("stats-text").textContent = msg;
  } else {
    bar.classList.add("hidden");
  }
}

async function renderGrid() {
  const raw = await pyodide.runPythonAsync("get_grid()");
  const grid = JSON.parse(raw);
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      const cell = document.getElementById(`cell-${r}-${c}`);
      cell.className = "cell";
      if (grid[r][c] === 1) cell.classList.add("p1");
      if (grid[r][c] === 2) cell.classList.add("p2");
    }
  }
}

function setButtonsDisabled(disabled) {
  document.querySelectorAll(".col-btn").forEach(b => b.disabled = disabled);
}

async function humanMove(col) {
  if (gameOver || !playerTurn) return;
  const validRaw = await pyodide.runPythonAsync("valid_moves_list()");
  const valid = JSON.parse(validRaw);
  if (!valid.includes(col)) return;

  setButtonsDisabled(true);
  await pyodide.runPythonAsync(`apply_human_move(${col})`);
  await renderGrid();

  const terminal = await pyodide.runPythonAsync("is_terminal()");
  if (terminal) { await endGame(); return; }

  playerTurn = false;
  await aiMove();
}

async function aiMove() {
  const depth = parseInt(document.getElementById("depth-select").value);
  setStatus("AI thinking...");
  // yield to browser to repaint before blocking
  await new Promise(r => setTimeout(r, 20));

  const raw = await pyodide.runPythonAsync(`get_ai_move(${depth})`);
  const result = JSON.parse(raw);
  await renderGrid();

  setStats(`AI played column ${result.move} — ${result.nodes.toLocaleString()} nodes visited, ${result.pruned.toLocaleString()} pruned (${result.time}s)`);

  const terminal = await pyodide.runPythonAsync("is_terminal()");
  if (terminal) { await endGame(); return; }

  playerTurn = true;
  setButtonsDisabled(false);
  setStatus("Your turn");
}

async function endGame() {
  gameOver = true;
  setButtonsDisabled(true);
  const winner = await pyodide.runPythonAsync("get_winner()");
  if (winner === 1) setStatus("You win!");
  else if (winner === 2) setStatus("AI wins!");
  else setStatus("Draw!");
}

async function newGame() {
  gameOver = false;
  playerTurn = true;
  await pyodide.runPythonAsync("reset()");
  await renderGrid();
  setStats(null);
  setButtonsDisabled(false);
  setStatus("Your turn — click a column");
}

init();