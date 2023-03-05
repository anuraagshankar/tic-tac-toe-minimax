"""
    Minimax bot file
"""
from board import Board


class Bot:
    """
    Bot class to play against
    """

    def __init__(self, player):
        self.__player = player
        self.__opponent_player = 1 if self.__player == 0 else 0
        self.__board = Board()

    def add_player_move(self, x, y):
        """
        Add the opponent player's move
        Args:
            x (int): X-coordinate of move
            y (int): Y-coordinate of move
        """
        self.__board.move(x, y, self.__opponent_player)

    def get_bot_move(self):
        """
        Obtain bot move
        Returns:
            x (int): X-coordinate of move
            y (int): Y-coordinate of move
        """
        moves = self.__board.get_moves()
        max_value = -1000
        best_x, best_y = -1, -1
        for x, y in moves:
            value = self.__minimax(self.__board, x, y, maximizing=False)
            if value > max_value:
                max_value = value
                best_x, best_y = x, y
        self.__board.move(best_x, best_y, self.__player)
        return best_x, best_y

    def __minimax(self, board: Board, x, y, maximizing=True):
        """
        Minimax algorithm to decide which move is the best
        Args:
            board (Board): Current board configuration
            x (int): X-coordinate of move
            y (int): Y-coordinate of move
            maximizing (bool, optional): Whether current move is of the maximizer. Defaults to True.
        Returns:
            int: Best possible value for the current player
        """
        new_board = board.copy()
        cur_player = self.__player if not maximizing \
            else self.__opponent_player
        new_board.move(x, y, cur_player)
        moves = new_board.get_moves()
        if new_board.winner != -1:
            return self.__get_board_value(new_board)

        if maximizing:
            max_value = -1000
            for new_x, new_y in moves:
                max_value = max(max_value, self.__minimax(
                    new_board, new_x, new_y, maximizing=False))
            return max_value
        else:
            min_value = 1000
            for new_x, new_y in moves:
                min_value = min(min_value, self.__minimax(
                    new_board, new_x, new_y, maximizing=True))
            return min_value

    def __get_board_value(self, board: Board):
        """
        Get the completed board value
        Args:
            board (Board): Completed board configuration
        Returns:
            int: Board value
        """
        winner = board.winner
        if winner == self.__player:
            return 1
        elif winner == self.__opponent_player:
            return -1
        return 0
