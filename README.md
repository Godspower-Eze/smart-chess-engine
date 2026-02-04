# Chess Engine

A chess engine built from scratch in Python using Minimax with Alpha-Beta pruning.

## Features

- Full chess rules implementation (castling, en passant, promotion)
- Move generation and validation
- CLI interface for playing against the engine
- Minimax search with Alpha-Beta pruning
- Material and positional evaluation

## Project Structure

```
chess-engine/
├── src/
│   ├── constants.py    # Piece codes, colors, board constants
│   ├── board.py        # Board state, make/undo move
│   ├── move.py         # Move representation
│   ├── move_gen.py     # Move generation
│   └── engine.py       # AI (Minimax, Evaluation)
├── main.py             # CLI game loop
└── tests/              # Unit tests
```

## Usage

```bash
python main.py
```

## License

MIT
