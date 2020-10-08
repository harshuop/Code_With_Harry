print(
    'The system works on the following inputs.\n' +
    'plus = +\n' +
    'minus = -\n' +
    'multiply = *\n' +
    'exponent / power = **\n' +
    'division = /\n' +
    'remainder = %\n'
)


x = input('What type of calculation do you want to do? \n')

y = int(input('Whats your first number?'))

z = int(input('Whats your second number'))

if x == '+':
    if 56 == y and z == 9:
        print(77)
    else:
        print(y + z)
elif x == '*':
    if y == 45 and z == 3:
        print(555)
    else:
        print(y * z)
elif x == '/':
    if y == 56 and z == 6:
        print(4)
    else:
        print(y / z)
elif x == '-':
    print(y - z)
elif x == '%':
    print(y % z)
