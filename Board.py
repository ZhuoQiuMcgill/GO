import numpy as np


class Board:

    #1 黑棋
    #-1 白棋
    #0 无子
    def __init__(self, size):
        self.board = np.zeros((size, size), dtype=int)
        self.next_player = 1

        #打劫
        self.last_Ko_x = None
        self.last_Ko_y = None

    def black_move(self, x, y):
        if x == self.last_Ko_x and y == self.last_Ko_y:
            return "Ko error"
        elif self.board[x][y] != 0:
            return "Stone error"
        else:
            self.board[x][y] = 1
            self.check_capture(self, 1)
            self.next_player = -1

    def white_move(self, x, y):
        if x == self.last_Ko_x and y == self.last_Ko_y:
            return "Ko error"
        elif self.board[x][y] != 0:
            return "Stone error"
        else:
            self.board[x][y] = -1
            self.check_capture(self, -1)
            self.next_player = 1

    def check_capture(self, current_player):
        if current_player == 1:
            return
        elif current_player == -1:
            return
        else:
            return

    def stop(self, next_player):
        if self.next_player == 1:
            self.next_player = -1
        elif self.next_player == -1:
            self.next_player = 1


