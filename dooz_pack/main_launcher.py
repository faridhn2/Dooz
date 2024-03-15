from dooz_pack.main_player import Player
from dooz_pack.main_checker import Checker
from dooz_pack.main_board import Board
from dooz_pack.main_display import Display
class Launcher:
  def __init__(self,player_names):
    print('Welcome')

    self.board = Board()
    print('create board')
    self.players = []
    for player_name in player_names:
      player = Player(player_name)
      self.players.append(player)
    print(' Vs. '.join([str(player) for player in self.players]))
    print('create players')

    # players = [Player(player_name) for player_name in player_names  ]
    markers = self.players[0].select_marker()
    self.players[1].marker = markers[1]
    print(markers)
    print('set Markers ')

    self.checker = Checker(self.players)
    print('create checker')

  def game(self):
    self.checker.new_game()
    self.board.clear()
    
    turn_player = self.checker.first_player()
    self.display = Display(self.checker.number_of_game)

    while not self.checker.game_ended:
      self.display.display_board(self.board.board,turn_player)

      position = turn_player.choose_position(self.board)
      self.board.place_marker(turn_player.marker,position)
      self.display.display_board(self.board.board,turn_player)
      win = turn_player.cal_score(self.checker,self.board)
      if not win :
        is_tie = self.checker.tie(self.board)
      
      turn_player = self.checker.change_turn()
    
    if is_tie:
        winner = None
    else:
        winner_name = self.checker.last_winner
        winner = list(filter(lambda player:player.name==winner_name,self.players))[0]
        
    self.display.display_result(self.players,winner)





