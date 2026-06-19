"""Cho-Han, modified by Peter Ddamulira
Assignment: Module 3.2 - Brownfield + Flowchart
Changes made:
1. Changed user input prompt to PD:
2. Changed house fee from 10% to 12%.
3. Added a 10 mon bonus when dice total equals 2 or 7.
4. Added bonus notice to the program introduction.
"""

import random
import sys

JAPANESE_NUMBERS = {
    1: 'ICHI', 2: 'NI', 3: 'SAN',
    4: 'SHI', 5: 'GO', 6: 'ROKU'
}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com
Modified by Peter Ddamulira

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

Bonus Rule: If the dice roll total is 2 or 7, the player receives
a 10 mon bonus added to their purse.
''')

purse = 5000

while True:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')

    while True:
        pot = input('PD: ')

        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('PD: ').upper()

        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Bonus rule added for dice totals of 2 or 7.
    if dice_total == 2 or dice_total == 7:
        print('The dice total was', dice_total)
        print('Bonus! You received 10 mon.')
        purse = purse + 10

    rollIsEven = dice_total % 2 == 0

    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot

        # House fee changed from 10% to 12%.
        house_fee = int(pot * 0.12)
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee
    else:
        purse = purse - pot
        print('You lost!')

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()