from termcolor import colored
# from IPython.display import clear_output 
# for vscode:
import os
from dooz_pack.main_player import Player

class Display():
    '''
    This class is for displaying board, the winner, the current turn, score of players, and number of games
    '''


    def __init__(self, number_of_games):
        self.number_of_games = number_of_games

    def display_board(self, board:list, turn:Player):
        os.system('cls')
        
        self.display_n_of_games()
        self.display_turn(turn)
        
        print(board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('---------')
        print(board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('---------')
        print(board[1] + ' | ' + board[2] + ' | ' + board[3])

    def display_turn(self,turn):
        print(colored(f'turn is for {turn}', 'blue'))

    def display_result(self,players,winner:Player):
        if winner:
            out_str = colored('','blue')
            for player in players:
                if player == winner:
                    out_str += colored(f" {player.name}", 'green')
                else:
                    out_str += colored(f" {player.name}", 'red')
        else:
            print(colored('    Tie ','blue'))
            out_str =  colored('','blue')
            for player in players:
                
                out_str += colored(f" {player.name}", 'blue')
                
        print(out_str)
        self.show_emojies(players,winner)
        self.show_scores(players)
    
    def show_emojies(self,players, winner:Player):
        if winner:
            out_str = ''
            for player in players:
                if player == winner:
                    out_str += '   😄   '
                else:
                    out_str += '  😒  '
                
        else:
            out_str = ''
            for player in players:
                
                 out_str += '   😐   '
                
        print(out_str)


    def display_n_of_games(self):
        print(f"Game No. {self.number_of_games}")

    def show_scores(self,players):
        players = sorted(players,key=lambda player: player.score,reverse=True)
        print(colored(f"The score of {players[0]} is {players[0].score}", 'green'))
        print(colored(f"The score of {players[1]} is {players[1].score}", 'red'))



