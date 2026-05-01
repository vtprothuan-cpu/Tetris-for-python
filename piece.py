# --- piece.py ---
import random
import settings # Gọi file settings.py do Đào làm

# 1. Khai báo Ma trận các khối gạch
S = [['.....', '.....', '..00.', '.00..', '.....'],
     ['.....', '..0..', '..00.', '...0.', '.....']]

Z = [['.....', '.....', '.00..', '..00.', '.....'],
     ['.....', '...0.', '..00.', '..0..', '.....']]

I = [['..0..', '..0..', '..0..', '..0..', '.....'],
     ['.....', '0000.', '.....', '.....', '.....']]

O = [['.....', '.....', '.00..', '.00..', '.....']]

J = [['.....', '.0...', '.000.', '.....', '.....'],
     ['.....', '..00.', '..0..', '..0..', '.....'],
     ['.....', '.....', '.000.', '...0.', '.....'],
     ['.....', '..0..', '..0..', '.00..', '.....']]

L = [['.....', '...0.', '.000.', '.....', '.....'],
     ['.....', '..0..', '..0..', '..00.', '.....'],
     ['.....', '.....', '.000.', '.0...', '.....'],
     ['.....', '.00..', '..0..', '..0..', '.....']]

T = [['.....', '..0..', '.000.', '.....', '.....'],
     ['.....', '..0..', '..00.', '..0..', '.....'],
     ['.....', '.....', '.000.', '..0..', '.....'],
     ['.....', '..0..', '.00..', '..0..', '.....']]

SHAPES = [S, Z, I, O, J, L, T]

# Màu sắc tương ứng với từng khối
SHAPE_COLORS = [    
    (0, 255, 0),   # S
    (255, 0, 0),   # Z
    (0, 255, 255), # I
    (255, 255, 0), # O
    (0, 0, 255),   # J
    (255, 165, 0), # L
    (128, 0, 128)  # T
]

# 2. Xây dựng Class Piece
class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = SHAPE_COLORS[SHAPES.index(shape)]
        self.rotation = 0 # Luôn bắt đầu ở hình thái xoay đầu tiên (index 0)

    def get_formatted_shape(self):
        return self.shape[self.rotation % len(self.shape)]
    # Hàm sẽ xử lí như sau: Kiểm tra khối đang xét (vd là khối S --> len(self.shapr) = 2)
    # 1. người chơi bấm 1 lần --> self.rotation = 1 --> làm thuật toán chia dư --> self.shape[1] --> đảo 90 độ và là chuỗi index = 1
    # 2. người chơi bấm 2 lần --> self.rotation = 2 --> làm thuật toán chia dư --> self.shape[0] --> đảo lại thành nguyên mẫu

def get_random_piece(): #hàm tạo gạch random
    # Lấy số cột chia đôi (10 / 2 = 5) làm tọa độ X, bắt đầu từ hàng 0
    return Piece(settings.COLUMNS // 2, 0, random.choice(SHAPES))