import pygame
from Board import *
from Constant import *

# 初始化 Pygame
pygame.init()

# 定义棋盘和棋子的大小
CELL_SIZE = 30
BOARD_LENGTH = (BOARD_SIZE - 1) * CELL_SIZE
PIECE_SIZE = CELL_SIZE // 2.2

# 定义棋盘左上角位置
X_OFFSET = 50
Y_OFFSET = 50

# 初始化棋盘
MEMORY = [[]]
CURRENT_BOARD = []
GAME_BOARD = Board(BOARD_SIZE)
CURRENT_COLOR = BLACK
BLACK_POS, WHITE_POS = [], []
STEP_COUNTER = 0


# 计算窗口的大小
WINDOW_SIZE = 800

# 创建窗口
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
running = True

# 设置窗口标题
pygame.display.set_caption('围棋')


# 棋盘渲染方程
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

    # 渲染当前颜色
    x_offset = X_OFFSET + CELL_SIZE * 9
    y_offset = Y_OFFSET - CELL_SIZE

    pygame.draw.circle(window, BLACK, (x_offset, y_offset), PIECE_SIZE)
    pygame.draw.circle(window, CURRENT_COLOR, (x_offset, y_offset), PIECE_SIZE - 1)


# 棋子渲染方程
def draw_piece(x, y, color):
    position = (X_OFFSET + x * CELL_SIZE, Y_OFFSET + y * CELL_SIZE)

    if color == WHITE:
        pygame.draw.circle(window, BLACK, position, PIECE_SIZE)
        pygame.draw.circle(window, WHITE, position, PIECE_SIZE - 1)
    else:
        pygame.draw.circle(window, BLACK, position, PIECE_SIZE)


def draw_territory(b_t, w_t):
    rect_size = CELL_SIZE // 3
    for x, y in b_t:
        center = (X_OFFSET + x * CELL_SIZE, Y_OFFSET + y * CELL_SIZE)
        left = center[0] - rect_size // 2
        top = center[1] - rect_size // 2

        pygame.draw.rect(window, BLACK, pygame.Rect(left, top, rect_size, rect_size))

    for x, y in w_t:
        center = (X_OFFSET + x * CELL_SIZE, Y_OFFSET + y * CELL_SIZE)
        left = center[0] - rect_size // 2
        top = center[1] - rect_size // 2
        pygame.draw.rect(window, WHITE, pygame.Rect(left, top, rect_size, rect_size))


def position_translate(x, y):
    if x < X_OFFSET or x > X_OFFSET + BOARD_LENGTH or y < Y_OFFSET or y > Y_OFFSET + BOARD_LENGTH:
        return -1, -1

    x_board = (x - X_OFFSET + CELL_SIZE / 2) // CELL_SIZE
    y_board = (y - Y_OFFSET + CELL_SIZE / 2) // CELL_SIZE
    return int(x_board), int(y_board)


# 主程序循环
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 处理其他事件，例如鼠标点击，添加棋子等
        if event.type == pygame.MOUSEBUTTONDOWN:

            # 左键下棋
            if event.button == 1:  # 1 代表鼠标左键
                GAME_BOARD.translate(MEMORY[-1])
                x_pos, y_pos = event.pos
                x_board, y_board = position_translate(x_pos, y_pos)
                if (x_board, y_board) == (-1, -1):
                    continue

                # 添加黑子
                if CURRENT_COLOR == BLACK:
                    new_board = GAME_BOARD.black_move(x_board, y_board)
                    if type(new_board) is str:
                        print(new_board)
                        continue
                    MEMORY.append(new_board[:])
                    CURRENT_COLOR = WHITE

                # 添加白子
                elif CURRENT_COLOR == WHITE:
                    new_board = GAME_BOARD.white_move(x_board, y_board)
                    if type(new_board) is str:
                        print(new_board)
                        continue
                    MEMORY.append(new_board[:])
                    CURRENT_COLOR = BLACK

                # 当前步数加一
                STEP_COUNTER += 1

                # 计算目数
                black_territory, white_territory, BLACK_POS, WHITE_POS = GAME_BOARD.count_territory()

                print("Step", STEP_COUNTER, "( Black:", black_territory, "\tWhite:", white_territory, ")")


            # 右键悔棋
            elif event.button == 3:  # 3 代表鼠标右键
                if len(MEMORY) > 1:

                    # 返回到上一个行动条
                    MEMORY.remove(MEMORY[-1])

                    # 变更颜色
                    if CURRENT_COLOR == WHITE:
                        CURRENT_COLOR = BLACK
                    else:
                        CURRENT_COLOR = WHITE

                # 当前步数减一
                STEP_COUNTER -= 1

                # 更新后端棋盘
                GAME_BOARD.translate(MEMORY[-1])

                # 计算目数
                black_territory, white_territory, BLACK_POS, WHITE_POS = GAME_BOARD.count_territory()

    # 清空窗口
    window.fill((222, 184, 135))

    # 渲染棋盘
    draw_board()

    # 渲染棋子
    for x, y, color in MEMORY[-1]:
        draw_piece(x, y, color)

    # 渲染地盘
    draw_territory(BLACK_POS, WHITE_POS)

    # 更新显示
    pygame.display.flip()

pygame.quit()
