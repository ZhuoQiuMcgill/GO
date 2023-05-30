import pygame
from Board import *

# 初始化 Pygame
pygame.init()

# 定义棋盘和棋子的大小
BOARD_SIZE = 19
CELL_SIZE = 30
BOARD_LENGTH = (BOARD_SIZE - 1) * CELL_SIZE
PIECE_SIZE = CELL_SIZE // 2.2

# 定义棋盘左上角位置
X_OFFSET = 50
Y_OFFSET = 50

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 计算窗口的大小
WINDOW_SIZE = 800

# 创建窗口
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# 设置窗口标题
pygame.display.set_caption('围棋')


def draw_board():
    for i in range(BOARD_SIZE):

        # 竖线
        pygame.draw.line(window, BLACK,
                         (i * CELL_SIZE + X_OFFSET, Y_OFFSET),
                         (i * CELL_SIZE + X_OFFSET, Y_OFFSET + BOARD_LENGTH))

        # 横线
        pygame.draw.line(window, BLACK,
                         (X_OFFSET, i * CELL_SIZE + Y_OFFSET),
                         (X_OFFSET + BOARD_LENGTH, i * CELL_SIZE + Y_OFFSET))

    # 边框
    offset = 10
    line_width = 2
    pygame.draw.line(window, BLACK,
                     (X_OFFSET - offset, Y_OFFSET - offset),
                     (X_OFFSET + BOARD_LENGTH + offset, Y_OFFSET - offset),
                     line_width)
    pygame.draw.line(window, BLACK,
                     (X_OFFSET + BOARD_LENGTH + offset, Y_OFFSET - offset),
                     (X_OFFSET + BOARD_LENGTH + offset, Y_OFFSET + BOARD_LENGTH + offset),
                     line_width)
    pygame.draw.line(window, BLACK,
                     (X_OFFSET + BOARD_LENGTH + offset, Y_OFFSET + BOARD_LENGTH + offset),
                     (X_OFFSET - offset, Y_OFFSET + BOARD_LENGTH + offset),
                     line_width)
    pygame.draw.line(window, BLACK,
                     (X_OFFSET - offset, Y_OFFSET + BOARD_LENGTH + offset),
                     (X_OFFSET - offset, Y_OFFSET - offset),
                     line_width)

    # 星位
    point_size = 4
    points = [
        (3, 3),
        (3, 9),
        (3, 15),
        (9, 3),
        (9, 9),
        (9, 15),
        (15, 3),
        (15, 9),
        (15, 15)
    ]
    for x, y in points:
        position = (X_OFFSET + x * CELL_SIZE, Y_OFFSET + y * CELL_SIZE)
        pygame.draw.circle(window, BLACK, position, point_size)


def draw_piece(x, y, color):
    position = (X_OFFSET + x * CELL_SIZE, Y_OFFSET + y * CELL_SIZE)

    if color == WHITE:
        pygame.draw.circle(window, BLACK, position, PIECE_SIZE)
        pygame.draw.circle(window, WHITE, position, PIECE_SIZE - 1)
    else:
        pygame.draw.circle(window, BLACK, position, PIECE_SIZE)


def position_translate(x, y):
    if x < X_OFFSET or x > X_OFFSET + BOARD_LENGTH or y < Y_OFFSET or y > Y_OFFSET + BOARD_LENGTH:
        return -1, -1

    x_board = (x - X_OFFSET + CELL_SIZE / 2) // CELL_SIZE
    y_board = (y - Y_OFFSET + CELL_SIZE / 2) // CELL_SIZE
    return x_board, y_board


# 初始化棋盘
# (x, y, BLACK/WHITE)
BOARD = []
GAME_BOARD = Board(BOARD_SIZE)

running = True
current_color = BLACK
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 处理其他事件，例如鼠标点击，添加棋子等
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 左键下棋
            if event.button == 1:  # 1 代表鼠标左键
                x_pos, y_pos = event.pos
                x_board, y_board = position_translate(x_pos, y_pos)
                print(x_board, y_board)

                # 添加黑子
                if current_color == BLACK and ((x_board, y_board, BLACK) not in BOARD
                                               and (x_board, y_board, WHITE) not in BOARD):
                    BOARD.append((x_board, y_board, current_color))
                    current_color = WHITE

                # 添加白子
                elif current_color == WHITE and ((x_board, y_board, BLACK) not in BOARD
                                                 and (x_board, y_board, WHITE) not in BOARD):
                    BOARD.append((x_board, y_board, current_color))
                    current_color = BLACK
                    
            # 右键悔棋
            elif event.button == 3:  # 3 代表鼠标右键
                if len(BOARD) > 0:
                    BOARD.remove(BOARD[-1])
                    if current_color == WHITE:
                        current_color = BLACK
                    else:
                        current_color = WHITE

    # 清空窗口
    window.fill((222, 184, 135))

    # 绘制棋盘
    draw_board()

    # 绘制棋子
    for x, y, color in BOARD:
        draw_piece(x, y, color)

    # 更新显示
    pygame.display.flip()

pygame.quit()
