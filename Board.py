import numpy as np


class Board:

    #1 黑棋
    #-1 白棋
    #0 无子
    def __init__(self, size):
        self.size = size
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
            self.check_capture(self, 1, x, y)
            self.next_player = -1

    def white_move(self, x, y):
        if x == self.last_Ko_x and y == self.last_Ko_y:
            return "Ko error"
        elif self.board[x][y] != 0:
            return "Stone error"
        else:
            self.board[x][y] = -1
            self.check_capture(self, -1, x, y)
            self.next_player = 1

    def check_capture(self, current_player, x, y):
        capt_num = 0
        top = self.board[x - 1, y] if x > 0 else None
        bottom = self.board[x + 1, y] if x < self.size - 1 else None
        left = self.board[x, y - 1] if y > 0 else None
        right = self.board[x, y + 1] if y < self.size - 1 else None
        if current_player == 1:
            if top == -1:
                self.check_suicide(self, current_player, x - 1, y)
            if bottom == -1:
                self.check_suicide(self, current_player, x + 1, y)
            if left == -1:
                self.check_suicide(self, current_player, x, y - 1)
            if right == -1:
                self.check_suicide(self, current_player, x, y + 1)
        elif current_player == -1:
            if top == 1:
                self.check_suicide(self, current_player, x - 1, y)
            if bottom == 1:
                self.check_suicide(self, current_player, x + 1, y)
            if left == 1:
                self.check_suicide(self, current_player, x, y - 1)
            if right == 1:
                self.check_suicide(self, current_player, x, y + 1)
        else:
            return

    def check_suicide(self, current_player, x, y):






    def stop(self, next_player):
        if self.next_player == 1:
            self.next_player = -1
        elif self.next_player == -1:
            self.next_player = 1


