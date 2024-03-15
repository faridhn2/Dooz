from dooz_pack.main_board import Board
from dooz_pack.main_checker import Checker
class Player:
    """
    class Player
    attrs : { marker: None | 'O' | 'X', score:number, name:str, turn:bool }
    methods : { __str__, choose_position, select_marker, cal_score }
    """
    def __init__(self,name):
        self.marker = None
        self.name = name
        self.score = 0
        self.turn = False
    
    def __str__(self):
        """
        Desc: returns the name of player
        Parameters: _
        Returns: name
        """
        return self.name 


    def choose_position(self, board: Board):
        """
        Desc: gets position from input, then decide whether it is in range 1-9 and the space in board is free, then returns the valid position
        Parameters: Board() as board,
        Returns: position
        """
        while True:
            position=input('Dear '+ self.name +' please choose a position:')
            if position.isdigit():
                position=int(position)
                if position in range(1,10) and board.free_space(position): 
                    return position

    def select_marker(self):
        """
        Desc: when the first user selects marker, a tuple of markers returns that specifies the user selections 
        Parameters: _
        Returns: ('X', 'O') or ('O', 'X')
        """        
        while True:
            player_sign = input(f'Dear {self.name}, choose X or O:')
            if player_sign in ['x','X']:
                self.marker = 'X'
                return ('X', 'O')
            elif player_sign in ['o','O']:
                self.marker = 'O'
                return ('O', 'X')

    def cal_score(self, checker: Checker, board: Board):
        """
        Desc: gets the board list from board object created from Board class, then checks a player is won. if yes score will be increased. then returns win=True 
        Parameters: checker(Checker()), board(Board())
        Returns: win: Boolean
        """
        board_list = board.board
        win = checker.win_check(board_list, self.name)
        if win:
            self.score += 1
        return win
    
