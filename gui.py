import pygame

# 初始化 Pygame
pygame.init()

# 定义棋盘和棋子的大小
BOARD_SIZE = 19
CELL_SIZE = 30
BOARD_LENGTH = (BOARD_SIZE - 1) * CELL_SIZE
PIECE_SIZE = CELL_SIZE // 2.5

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 计算窗口的大小
WINDOW_SIZE = 800

# 创建窗口
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# 设置窗口标题
pygame.display.set_caption('围棋')


def draw_board(x_offset, y_offset):
    for i in range(BOARD_SIZE):

        # 竖线
        pygame.draw.line(window, BLACK,
                         (i * CELL_SIZE + x_offset, y_offset),
                         (i * CELL_SIZE + x_offset, y_offset + BOARD_LENGTH))

        # 横线
        pygame.draw.line(window, BLACK,
                         (x_offset, i * CELL_SIZE + y_offset),
                         (x_offset + BOARD_LENGTH, i * CELL_SIZE + y_offset))


def draw_piece(x_offset, y_offset, x, y, color):
    position = (x_offset + x * CELL_SIZE, y_offset + y * CELL_SIZE)
    pygame.draw.circle(window, color, position, PIECE_SIZE)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 处理其他事件，例如鼠标点击，添加棋子等
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 判断是否是鼠标左键被按下
            if event.button == 1:  # 1 代表鼠标左键
                x, y = event.pos
                print("Mouse left button clicked at position:", x, y)

    # 清空窗口
    window.fill((255, 255, 255))

    # 绘制棋盘
    draw_board(50, 50)

    # 绘制棋子
    # ... 这里根据游戏的状态，调用 draw_piece() 绘制棋子
    draw_piece(50, 50, 9, 9, BLACK)
    draw_piece(50, 50, 0, 0, BLACK)
    # 更新显示
    pygame.display.flip()

pygame.quit()
