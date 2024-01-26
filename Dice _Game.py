import random

def main():

    PlayerOne = input('Player One:')
    print('Hello, ' + PlayerOne)

    PlayerTwo = input('Player Two:')
    print('Hello, ' + PlayerTwo)
    p1 = 0
    winsPlayer1 = 0
    p2 = 0
    winsPlayer2 = 0

    rounds = 1



    while rounds != 4:
        print('round ' + str(rounds))

        p1 = roll_dice()
        p2 = roll_dice()
        print(PlayerOne + ' Roll: ' + str(p1))
        print(PlayerTwo + ' Roll: ' + str(p2))

        if p1 > p2:
            print(PlayerOne + ' Wins')
            winsPlayer1 = winsPlayer1 + 1

        elif p2 > p1:
            print(PlayerTwo + ' Wins')
            winsPlayer2 = winsPlayer2 + 1

        else:
            print('Draw')

        rounds = rounds + 1
        
    if winsPlayer1 > winsPlayer2:
         print('It\'s all over; ' + PlayerOne + ' Wins')


    elif winsPlayer2 > winsPlayer1:
        print('It\'s all over; ' + PlayerTwo + ' Wins')

    else:
        print('Perfectly balanced as all things should be')
        




def roll_dice():
    dice = random.randint(1, 6)
    return dice

main()