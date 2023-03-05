
"""
Tic-Tac-Toe board to play the game
"""
import copy


class Board:
    """
    Tic-Tac-Toe board class
    """

    def __init__(self):
        self.__board = [[-1 for _ in range(3)] for _ in range(3)]
        self.__current_player = 0
        self.__winner = -1

    @property
    def board(self):
        """
        Get the current board state
        Returns:
            2d List: Board array
        """
        return self.__board

    @property
    def winner(self):
        """
        Get the winner if exists
        Returns:
            int: Winner if exists, else -1
        """
        return self.__winner

    def move(self, x, y, player):
        """
        Move of the current player
        Args:
            x (int): X-coordinate of move
            y (int): Y-coordinate of move
        Returns:
            int: Winner if exists, else -1
        """
        assert self.__board[x][y] == -1, "Board position occupied."
        assert self.__winner == -1, "Game complete."
        assert player == self.__current_player, "Incorrect player move."
        self.__board[x][y] = self.__current_player
        self.__winner = self.__check_winner()
        self.__current_player = 1 if self.__current_player == 0 else 0
        return self.__winner

    def __check_winner(self):
        """
        Board validations
        Returns:
            int: Winner if exists, else -1
        """
        # Row-wise checking
        for i in range(3):
            if self.__board[i][0] == self.__board[i][1] \
                and self.__board[i][1] == self.__board[i][2] \
                    and self.__board[i][0] != -1:
                return self.__board[i][0]

        # Column-wise checking
        for i in range(3):
            if self.__board[0][i] == self.__board[1][i] \
                and self.__board[1][i] == self.__board[2][i] \
                    and self.__board[0][i] != -1:
                return self.__board[0][i]

        # Diagonal 1 check
        if self.__board[0][0] == self.__board[1][1] \
            and self.__board[1][1] == self.__board[2][2] \
                and self.__board[0][0] != -1:
            return self.__board[0][0]

        # Diagonal 2 check
        if self.__board[0][2] == self.__board[1][1] \
            and self.__board[1][1] == self.__board[2][0] \
                and self.__board[0][2] != -1:
            return self.__board[0][2]

        if self.__is_draw():
            return 2

        return -1

    def __is_draw(self):
        draw = True
        for i in range(3):
            for j in range(3):
                if self.__board[i][j] == -1:
                    draw = False
        return draw

    def get_moves(self):
        """
        Get all possible valid moves
        Returns:
            list: List of valid move tuples
        """
        moves = []
        for i in range(3):
            for j in range(3):
                if self.__board[i][j] == -1:
                    moves.append((i, j))
        return moves

    def copy(self):
        """
        Returns copy of the current board object

        Returns:
            Board: Current board configuration
        """
        return copy.deepcopy(self)
