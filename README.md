# 🎮 Tic Tac Toe — Terminal Edition

A stylish terminal Tic Tac Toe game built with Python and the [Rich](https://github.com/Textualize/rich) library. Play against a smart AI opponent that fights back — all inside your console.

---

## ✨ Features

- 🎨 **Rich-powered UI** — colored panels, styled tables, and live spinners make the terminal feel alive
- 🤖 **Smart AI opponent** — uses a Win → Block → Random strategy so it never throws a game away
- ♟️ **Numbered position guide** — the board always shows available cell numbers so you never lose track
- ⏳ **AI "thinking" animation** — a bouncing-bar spinner adds dramatic flair before the computer moves
- 🔁 **Play again prompt** — jump straight into a rematch or exit gracefully after each game

---

## 🧠 AI Algorithm — Win → Block → Random

The AI evaluates the board in three priority steps every turn:

```
1. WIN    — Scan every empty cell. If placing O there wins the game, take it immediately.
2. BLOCK  — Scan every empty cell. If placing X there would let the player win, block it.
3. RANDOM — No critical move found? Pick a random empty cell.
```

This is implemented cleanly with the same `check()` function used for win detection — the AI simulates a move, tests for a win, then undoes it if the condition isn't met.

---

## 🖼️ Rich Components Used

| Component | How it's used in the game |
|---|---|
| `Console` | Central renderer for all output |
| `Panel` | Welcome screen and "GAME START" banner |
| `Table` + `box.DOUBLE` | Static position-reference board shown at startup |
| `Table` + `box.SQUARE` | Live game board updated after every move |
| `console.status` + `spinner="bouncingBar"` | AI "thinking..." animation with a 3-second delay |
| Rich markup (`[bold green]`, `[dim]`, etc.) | Color-coded X / O markers and styled prompts |

---

## 📋 Requirements

- Python 3.8+
- [Rich](https://github.com/Textualize/rich)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-rich.git
   cd tic-tac-toe-rich
   ```

2. **Install Rich**
   ```bash
   pip install rich
   ```

---

## 🚀 Usage

```bash
python main.py
```

---

## 🎮 How to Play

On launch you'll see a welcome panel and a position reference board:

```
╔═══╦═══╦═══╗
║ 1 ║ 2 ║ 3 ║
╠═══╬═══╬═══╣
║ 4 ║ 5 ║ 6 ║
╠═══╬═══╬═══╣
║ 7 ║ 8 ║ 9 ║
╚═══╩═══╩═══╝
```

- You are **X** (green), the computer is **O** (blue)
- Enter a number **1–9** to place your mark
- The live board replaces taken cells with X/O and keeps dim numbers on empty ones so you always know what's free
- After each game, you'll be asked `Do you want to continue? [Y/N]`

---

## 📁 Project Structure

```
tic-tac-toe-rich/
└── main.py      # Everything — board state, display, AI logic, and game loop
```

---

## 🔧 Key Functions

| Function | Responsibility |
|---|---|
| `display()` | Renders the current board state as a Rich `Table` |
| `check(player)` | Tests all 8 win conditions for a given player marker |
| `you()` | Handles player input, validation, and turn flow |
| `ai()` | Runs the Win → Block → Random logic and makes the computer's move |
| `con()` | Post-game prompt — resets board state and loops or exits |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
