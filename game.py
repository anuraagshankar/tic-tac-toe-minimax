"""
    Main file to run the game
"""
from board import Board


def int_to_symbol(x):
    """
    Get symbol from board position value
    Args:
        x (int): Board position value

    Returns:
        string: Board position symbol
    """
    if x == -1:
        return '_'
    elif x == 0:
        return 'X'
    elif x == 1:
        return 'O'
    else:
        return 'None'


def display_board(board):
    """
    Display board with proper characters

    Args:
        board (2d List): Board array
    """
    for i in range(3):
        for j in range(3):
            print(int_to_symbol(board[i][j]), end='\t')
        print()


if __name__ == '__main__':
    board = Board()
    while board.winner == -1:
        display_board(board.board)
        x = int(input("X-coordinate: "))
        y = int(input("Y-coordinate: "))
        board.move(x, y)
    display_board(board.board)
    print(f'Winner: {int_to_symbol(board.winner)}')
