import numpy as np
import StoneSet
from collections import deque
import Constant


class Board:

    # 1 黑棋
    # -1 白棋
    # 0 无子
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size), dtype=int)
        self.next_player = 1
        # self.stone_sets = []
        # for i in range (size):
        #     for j in range (size):
        #         self.stone_sets.append()

        # 打劫
        self.Ko = False
        self.last_Ko_x = None
        self.last_Ko_y = None

    def black_move(self, x, y):
        if self.Ko and x == self.last_Ko_x and y == self.last_Ko_y:
            return "Ko error"
        elif self.board[x][y] != 0:
            return "Stone error"
        self.board[x][y] = 1
        captured = self.check_capture(1, x, y)
        # 如果没有吃子，检测是否不入气
        if captured == 0:
            self.Ko = False
            if self.check_suicide(1, x, y) > 0:
                self.board[x][y] = 0
                return "Suicide error"
        # 如果只吃一子，检测打劫
        elif captured == 1:
            self.ko_check(x, y)
        else:
            self.Ko = False
        self.next_player = -1
        moves = []
        for i in range(Constant.BOARD_SIZE):
            for j in range(Constant.BOARD_SIZE):
                if self.board[i][j] == 1:
                    moves.append((i, j, Constant.BLACK))
                elif self.board[i][j] == -1:
                    moves.append((i, j, Constant.WHITE))
        return moves

    def white_move(self, x, y):
        if self.Ko and x == self.last_Ko_x and y == self.last_Ko_y:
            return "Ko error"
        elif self.board[x][y] != 0:
            return "Stone error"
        self.board[x][y] = -1
        captured = self.check_capture(-1, x, y)
        # 如果没有吃子，检测是否不入气
        if captured == 0:
            self.Ko = False
            if self.check_suicide(-1, x, y) > 0:
                self.board[x][y] = 0
                return "Suicide error"
        # 如果只吃一子，检测打劫
        elif captured == 1:
            self.ko_check(x, y)
        else:
            self.Ko = False
        self.next_player = 1
        moves = []
        for i in range(Constant.BOARD_SIZE):
            for j in range(Constant.BOARD_SIZE):
                if self.board[i][j] == 1:
                    moves.append((i, j, Constant.BLACK))
                elif self.board[i][j] == -1:
                    moves.append((i, j, Constant.WHITE))
        return moves

    def ko_check(self, x, y):
        count = 0
        if self.board[x - 1, y] if x > 0 else None == -1:
            count += 1
        else:
            pos = 1
        if self.board[x + 1, y] if x < self.size - 1 else None == -1:
            count += 1
        else:
            pos = 2
        if self.board[x, y - 1] if y > 0 else None == -1:
            count += 1
        else:
            pos = 3
        if self.board[x, y + 1] if y < self.size - 1 else None == -1:
            count += 1
        else:
            pos = 4
        if count == 3:
            self.Ko = True
            if pos == 1:
                self.last_Ko_x = x - 1
                self.last_Ko_y = y
            elif pos == 2:
                self.last_Ko_x = x + 1
                self.last_Ko_y = y
            elif pos == 3:
                self.last_Ko_x = x
                self.last_Ko_y = y - 1
            elif pos == 4:
                self.last_Ko_x = x
                self.last_Ko_y = y + 1
            else:
                print("bug")
        else:
            self.Ko = False

    # def move_union(self, current_player, x, y):
    #     top = self.board[x - 1, y] if x > 0 else None
    #     bottom = self.board[x + 1, y] if x < self.size - 1 else None
    #     left = self.board[x, y - 1] if y > 0 else None
    #     right = self.board[x, y + 1] if y < self.size - 1 else None
    #     # if top != current_player and bottom != current_player and left != current_player and right != current_player:
    #     #     self.stone_sets.append(StoneSet.StoneSet(x, y))
    #     else:
    #         if top == current_player:

    # 一步棋吃子的数量
    def check_capture(self, current_player, x, y):
        capt_num = 0
        top = self.board[x - 1, y] if x > 0 else None
        bottom = self.board[x + 1, y] if x < self.size - 1 else None
        left = self.board[x, y - 1] if y > 0 else None
        right = self.board[x, y + 1] if y < self.size - 1 else None
        if top == -current_player:
            capt_num += self.check_suicide(-current_player, x - 1, y)
        if bottom == -current_player:
            capt_num += self.check_suicide(-current_player, x + 1, y)
        if left == -current_player:
            capt_num += self.check_suicide(-current_player, x, y - 1)
        if right == -current_player:
            capt_num += self.check_suicide(-current_player, x, y + 1)
        # elif current_player == -1:
        #     if top == 1:
        #         capt_num += self.check_suicide(self, current_player, x - 1, y)
        #     if bottom == 1:
        #         capt_num += self.check_suicide(self, current_player, x + 1, y)
        #     if left == 1:
        #         capt_num += self.check_suicide(self, current_player, x, y - 1)
        #     if right == 1:
        #         capt_num += self.check_suicide(self, current_player, x, y + 1)
        print(capt_num)
        return capt_num

    # 检测一块棋是否还有气， BFS
    def check_suicide(self, current_player, x, y):
        visited = set()
        queue = deque([(x, y)])

        while queue:
            node = queue.popleft()
            print(queue)
            print(node)
            if node not in visited:
                x_val = node[0]
                y_val = node[1]
                top = self.board[x_val - 1, y_val] if x_val > 0 else None
                bottom = self.board[x_val + 1, y_val] if x_val < self.size - 1 else None
                left = self.board[x_val, y_val - 1] if y_val > 0 else None
                right = self.board[x_val, y_val + 1] if y_val < self.size - 1 else None
                print(top, bottom, left, right)
                visited.add(node)

                if top == 0 or bottom == 0 or left == 0 or right == 0:
                    return 0
                else:
                    if top == current_player and (x_val - 1, y_val) not in visited:
                        queue.append((x_val - 1, y_val))
                    if bottom == current_player and (x_val + 1, y_val) not in visited:
                        queue.append((x_val + 1, y_val))
                    if left == current_player and (x_val, y_val - 1) not in visited:
                        queue.append((x_val, y_val - 1))
                    if right == current_player and (x_val, y_val + 1) not in visited:
                        queue.append((x_val, y_val + 1))

        print(visited)
        for x_, y_ in visited:
            self.board[x_][y_] = 0
        return len(visited)

    def stop(self, next_player):
        if self.next_player == 1:
            self.next_player = -1
        elif self.next_player == -1:
            self.next_player = 1

    def translate(self, move_stack):
        temp_b = np.zeros((Constant.BOARD_SIZE, Constant.BOARD_SIZE), dtype=int)
        for m in move_stack:
            if m[2] == Constant.BLACK:
                temp_b[m[0]][m[1]] = 1
            elif m[2] == Constant.WHITE:
                temp_b[m[0]][m[1]] = -1
            else:
                print("convert error")
        self.board = temp_b
