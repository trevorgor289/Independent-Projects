from classes import Start_game


while True:
    player = input('would you like to play a game? Y/N:    ')
    if player == 'Y':
        start = Start_game()
        start.play_game()
    elif player == 'N':
        exit()
    else:
        print('Please choose Y/N')
