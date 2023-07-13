from story import startGame

i = 0

while i != 1:
    menuInput = input("[S]tart \n\n [Q]uit \n\n -> ")

    if menuInput == str():
        if menuInput == 'S':
            startGame()

    elif menuInput == 'Q':
        i = 1

