from cody import draw_board, check_turn
import os


spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
         6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
turn = 0

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    choice = input('Enter your choice: ')
    if choice == 'q':
        playing = False

    turn += 1
    spots[int(choice)] = check_turn(turn)