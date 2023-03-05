"""
    Main file to run the game
"""
from board import Board
from bot import Bot


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
    if x == 0:
        return 'X'
    if x == 1:
        return 'O'
    return 'None'


def display_board(game_board):
    """
    Display game board with proper characters

    Args:
        game_board (2d List): Board array
    """
    for i in range(3):
        for j in range(3):
            print(int_to_symbol(game_board[i][j]), end='\t')
        print()


if __name__ == '__main__':
    board = Board()
    bot = Bot(player=0)
    while board.winner == -1:
        x, y = bot.get_bot_move()
        board.move(x, y, player=0)
        display_board(board.board)
        print(f'Bot played: {x}, {y}')

        if board.winner != -1:
            break

        x = int(input('X-Coordinate: '))
        y = int(input('Y-Coordinate: '))
        board.move(x, y, player=1)
        bot.add_player_move(x, y)
        display_board(board.board)

    # while board.winner == -1:
    #     display_board(board.board)
    #     x = int(input('X-Coordinate: '))
    #     y = int(input('Y-Coordinate: '))
    #     board.move(x, y, player=0)

    #     if board.winner != -1:
    #         break

    #     bot.add_player_move(x, y)
    #     x, y = bot.get_bot_move()
    #     board.move(x, y, player=1)
    #     display_board(board.board)
    #     print(f'Bot played: {x}, {y}')
    display_board(board.board)
    print(f'Winner: {int_to_symbol(board.winner)}')
