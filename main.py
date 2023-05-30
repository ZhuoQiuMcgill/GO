import Board


def main():
    b = Board.Board(19)
    while True:
        move = input("Enter move: ")
        moves = move.split(",")
        b.board[3][3] = 1
        b.board[3][4] = -1
        b.board[3][2] = -1
        b.board[2][3] = -1
        if b.next_player == 1:
            b.black_move(int(moves[0]), int(moves[1]))
            print(b.board)
        elif b.next_player == -1:
            b.white_move(int(moves[0]), int(moves[1]))
            print(b.board)
        else:
            print("next player bug")


if __name__ == "__main__":
    main()
