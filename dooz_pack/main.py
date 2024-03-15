from dooz_pack.main_launcher import Launcher

def main():
    names = []
    for player_index in range(2):
        names.append(input(f'player{player_index+1} name?'))
        
    launcher = Launcher(names)
    while True:
        
        launcher.game()
        
        replay = input('play again? y/n')
        if not replay == 'y':
            break