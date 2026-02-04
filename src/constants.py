"""
Chess Engine Constants

Defines piece types, colors, and board layout constants.
"""

# Colors
WHITE = 0
BLACK = 1

# Piece types (0 = empty)
EMPTY = 0
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

# Combined piece codes: color * 8 + piece_type
# White pieces: 1-6, Black pieces: 9-14
def make_piece(color: int, piece_type: int) -> int:
    """Create a piece code from color and type."""
    return color * 8 + piece_type

def get_piece_color(piece: int) -> int:
    """Get the color of a piece (0=White, 1=Black)."""
    return piece // 8

def get_piece_type(piece: int) -> int:
    """Get the type of a piece (1=Pawn, 2=Knight, etc.)."""
    return piece % 8

# Pre-computed piece codes for convenience
WHITE_PAWN = make_piece(WHITE, PAWN)      # 1
WHITE_KNIGHT = make_piece(WHITE, KNIGHT)  # 2
WHITE_BISHOP = make_piece(WHITE, BISHOP)  # 3
WHITE_ROOK = make_piece(WHITE, ROOK)      # 4
WHITE_QUEEN = make_piece(WHITE, QUEEN)    # 5
WHITE_KING = make_piece(WHITE, KING)      # 6

BLACK_PAWN = make_piece(BLACK, PAWN)      # 9
BLACK_KNIGHT = make_piece(BLACK, KNIGHT)  # 10
BLACK_BISHOP = make_piece(BLACK, BISHOP)  # 11
BLACK_ROOK = make_piece(BLACK, ROOK)      # 12
BLACK_QUEEN = make_piece(BLACK, QUEEN)    # 13
BLACK_KING = make_piece(BLACK, KING)      # 14

# Piece values for evaluation (in centipawns)
PIECE_VALUES = {
    EMPTY: 0,
    PAWN: 100,
    KNIGHT: 320,
    BISHOP: 330,
    ROOK: 500,
    QUEEN: 900,
    KING: 20000,  # Effectively infinite
}

# Piece symbols for display
PIECE_SYMBOLS = {
    EMPTY: '.',
    WHITE_PAWN: 'P', WHITE_KNIGHT: 'N', WHITE_BISHOP: 'B',
    WHITE_ROOK: 'R', WHITE_QUEEN: 'Q', WHITE_KING: 'K',
    BLACK_PAWN: 'p', BLACK_KNIGHT: 'n', BLACK_BISHOP: 'b',
    BLACK_ROOK: 'r', BLACK_QUEEN: 'q', BLACK_KING: 'k',
}

# FEN piece mapping (for parsing)
FEN_PIECES = {
    'P': WHITE_PAWN, 'N': WHITE_KNIGHT, 'B': WHITE_BISHOP,
    'R': WHITE_ROOK, 'Q': WHITE_QUEEN, 'K': WHITE_KING,
    'p': BLACK_PAWN, 'n': BLACK_KNIGHT, 'b': BLACK_BISHOP,
    'r': BLACK_ROOK, 'q': BLACK_QUEEN, 'k': BLACK_KING,
}

# Reverse mapping for FEN generation
PIECE_TO_FEN = {v: k for k, v in FEN_PIECES.items()}

# Board dimensions
BOARD_SIZE = 64

# Starting position FEN
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# Square names (a1=0, h8=63)
def get_square_name(sq: int) -> str:
    """Convert square index to algebraic notation (e.g., 0 -> 'a1')."""
    file = sq % 8
    rank = sq // 8
    return chr(ord('a') + file) + str(rank + 1)

def get_name_from_square(name: str) -> int:
    """Convert algebraic notation to square index (e.g., 'a1' -> 0)."""
    file = ord(name[0]) - ord('a')
    rank = int(name[1]) - 1
    return rank * 8 + file

# Direction offsets for move generation (mailbox 64)
NORTH = 8
SOUTH = -8
EAST = 1
WEST = -1
NORTH_EAST = 9
NORTH_WEST = 7
SOUTH_EAST = -7
SOUTH_WEST = -9

# Knight move offsets
KNIGHT_OFFSETS = [
    NORTH + NORTH + EAST,   # +17
    NORTH + NORTH + WEST,   # +15
    SOUTH + SOUTH + EAST,   # -15
    SOUTH + SOUTH + WEST,   # -17
    EAST + EAST + NORTH,    # +10
    EAST + EAST + SOUTH,    # -6
    WEST + WEST + NORTH,    # +6
    WEST + WEST + SOUTH,    # -10
]

# King move offsets
KING_OFFSETS = [
    NORTH, SOUTH, EAST, WEST,
    NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST,
]

# Sliding piece directions
ROOK_DIRECTIONS = [NORTH, SOUTH, EAST, WEST]
BISHOP_DIRECTIONS = [NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST]
QUEEN_DIRECTIONS = ROOK_DIRECTIONS + BISHOP_DIRECTIONS

# Castling rights bitmask
CASTLE_WK = 1  # White kingside
CASTLE_WQ = 2  # White queenside
CASTLE_BK = 4  # Black kingside
CASTLE_BQ = 8  # Black queenside
