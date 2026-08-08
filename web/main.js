// MILESTONE M6.
//
// Rough plan (fill in as you get there — don't try to do this all at once):
//
// 1. Boot Pyodide and load the connect4 package:
//      const pyodide = await loadPyodide();
//      await pyodide.loadPackage("micropip");
//      const micropip = pyodide.pyimport("micropip");
//      await micropip.install("<url or path to a built connect4 wheel>");
//
// 2. Keep game state as a plain JS object (or re-derive it from Python
//    each move) and render it into #board as clickable cells.
//
// 3. On a human click: call into Python to apply the move, re-render,
//    then call choose_move() for the AI's reply, re-render again.
//
// 4. Wire up the #depth slider to the depth argument passed to
//    choose_move().
//
// Starting stub below just proves Pyodide itself loads correctly —
// replace once M1-M4 are done and there's an actual package to import.

async function main() {
  const status = document.getElementById("status");
  const pyodide = await loadPyodide();
  status.textContent = "Pyodide loaded. (Game logic not wired up yet — see TODOs in main.js)";
}

document.getElementById("depth").addEventListener("input", (e) => {
  document.getElementById("depth-label").textContent = e.target.value;
});

main();
