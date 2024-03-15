class Board:
    """
    A class representing a board, typically for board games like Tic Tac Toe.

    Attributes: board list[str]

    Methods:

    full(self):
        Returns: True if the board is full, False otherwise.

    free_space(self, position):

        Parameters: position (int)

        Returns: True if the specified position is free, False otherwise.

    clear(self):
        Clears the board by setting all positions, except the first, to be empty (indicated by ' ').

    place_marker(self, marker, position):
        Parameters: marker (str), position (int)
    """
    def __init__(self):
        self.clear()

    """
    Parameters: _
    Returns: Boolean 
    """
    def full(self):
    # check if the board is full to decide tie happened or not
        return ' ' not in self.board[1:]

    """
    Parameters: a number between 1-9 as position
    Returns: Boolean
    """
    def free_space(self, position):
    # check if there the seleted position is free
        return self.board[position] == ' '

    """
    Parameters: _
    Returns: _
    """
    def clear(self) -> None:
    # make the board list empty
        self.board = [' ']*10

    """
    Parameters: _
    Returns: _
    """
    # place the specific marker in selected position
    def place_marker(self, marker, position) -> None:
        self.board[position] = marker
