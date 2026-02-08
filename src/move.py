"""
Move representation for the chess engine.
"""

from dataclasses import dataclass
from src.constants import (
    EMPTY, KNIGHT, BISHOP, ROOK, QUEEN,
    get_square_name, get_square_from_name
)

promo_chars = {QUEEN: 'q', ROOK: 'r', BISHOP: 'b', KNIGHT: 'n'}
promo_map = {v: k for k, v in promo_chars.items()}

@dataclass
class Move:
    """
    Represents a chess move.
    
    Attributes:
        start: Starting square (0-63)
        end: Ending square (0-63)
        promotion: Piece type to promote to (QUEEN, ROOK, BISHOP, KNIGHT) or EMPTY
        is_castle: True if this is a castling move
        is_en_passant: True if this is an en passant capture
        captured: The captured piece (for undo), set when move is made
    """
    start: int
    end: int
    promotion: int = EMPTY
    is_castle: bool = False
    is_en_passant: bool = False
    captured: int = EMPTY  # Filled in when move is made
    
    def __str__(self) -> str:
        """Return move in UCI format (e.g., 'e2e4', 'e7e8q')."""
        s = get_square_name(self.start) + get_square_name(self.end)
        if self.promotion != EMPTY:
            s += promo_chars.get(self.promotion, '')
        return s
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Move):
            return False
        return (self.start == other.start and 
                self.end == other.end and 
                self.promotion == other.promotion)
    
    def __hash__(self) -> int:
        return hash((self.start, self.end, self.promotion))


def parse_move(uci: str) -> Move:
    """
    Parse a UCI move string (e.g., 'e2e4', 'e7e8q').
    
    Note: This creates a basic Move object. The is_castle and is_en_passant
    flags must be set by the move generator based on board state.
    """
    
    start = get_square_from_name(uci[0:2])
    end = get_square_from_name(uci[2:4])
    
    promotion = EMPTY
    if len(uci) == 5:
        promotion = promo_map.get(uci[4].lower(), EMPTY)
    
    return Move(start=start, end=end, promotion=promotion)

