import random

class Checker():
    """
    attrs: players: list[Player], number_of_games: number, game_ended: Boolean, last_winner: Player
    methods: tie, win_check, new_game, first_player, change_turn
    """
    def __init__(self, players): 
        self.players = players
        self.number_of_game = 0
        self.game_ended = False
        self.last_winner = None

    
    def tie(self, board):
        """
        Desc: based on board status, decide that the game is tie or not
        Parameters: board(Board)
        Returns: True, False
        """
        if  board.full():
            self.game_ended = True
            self.last_winner = None
            
            return True
        else: return False

    def win_check(self, board,name):
        """
        Desc: checks that whether the player with name has won the game
        Parameters: board:Board(), name: str
        Returns: True, False
        """
        winning_combination = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
        for player in self.players:
            if player.name == name:
                # iterate over players:list(Player) and gets the marker of that player with given name
                marker = player.marker         
                for combination in winning_combination:
                    # the ccondition that shows a player wins 
                    if board[combination[0]] == board[combination[1]] == board[combination[2]] == marker:
                        self.last_winner = player.name
                        self.game_ended = True
                        return True
                else: return False
        else: print("Not a Valid Player List")


    def new_game(self):
        """
        Desc: reset the player turns to False. increase number_of_games, set game_ended to False
        Parameters: _ 
        Returns: _
        """
        for player in self.players:
            player.turn = False
            
        self.number_of_game += 1
        self.game_ended = False 
        
    
    def first_player(self):
        """
        Desc: if there is no winner, it randomises between 2 players which one first to play. if there is a winner, he/she would be the first
        Parameters: _
        Returns: the chosen player (name_first_player)
        """
        if self.last_winner != None:
            for player in self.players:
                if player.name ==  self.last_winner:
                    player.turn = True
                    return player
        else:
            name_first_player = random.choice(self.players)
            name_first_player.turn = True
            return name_first_player

    def change_turn(self):
        """
        
        """
        for player in self.players:
          # player.turn =not (player.turn)
            if player.turn == True:
                player.turn = False
            else:
                player.turn = True

        for player in self.players:
            if player.turn == True:
              return player