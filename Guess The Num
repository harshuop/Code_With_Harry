y = 45
print('Your total number of chances = 9')
print('Chances you have used: ' + str(num) + '\n')

while True:
    i = int(input('\nWhat is the number you have guessed?\n'))

    num += 1

    if num < 9:
        if i < y:
            print('It is greater than ' + str(i) + '!')
        elif i > y:
            print('It is less than ' + str(i) + '!')
        else:
            print('Congratulations! You Won!')
            print('You have taken ' + str(num) + ' turns to complete it.')
            break
    else:
        print('Game Over')
        break
