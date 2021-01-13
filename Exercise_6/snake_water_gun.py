import random
import datetime

chances = 0
print(
    """
    Choose:
        Snake- 's'
        Water- 'w'
        Gun  - 'g'
    """
)
store = ['s','w','g']
computer_score = 0
player_score = 0
while True:
    ran = random.choice(store)
    if chances == 10:
        cod = f'Player Score: {player_score}\nComputer Score: {computer_score}'
        t = datetime.datetime.now()
        time = '  [' + str(t)[:-7] + ']\n'
        fill = time + cod
        with open('Exercise_6/game_history.txt', "a") as storage:
            storage.write(fill + '\n\n')
        print(cod)
        print('\n----------GAME-OVER----------')
        break
    elif chances != 10:
        choice = input('What do you choose: ')
        chances += 1
        if choice.lower() == ran:
            print('  -tie')
            pass
        elif choice.lower() == 's':
            if ran == 'w':
                player_score += 1
                print('  -player +1')
            elif ran == 'g':
                computer_score += 1
                print('  -computer +1')
        elif choice.lower() == 'w':
            if ran == 's':
                computer_score += 1
                print('  -computer +1')
            elif ran == 'g':
                player_score += 1
                print('  -player +1')
        else:
            if ran == 'w':
                computer_score += 1
                print('  -computer +1')
            elif ran == 's':
                player_score += 1
                print('  -player +1')
