import random

def cows_and_bulls():
    print('This is a Cows and Bulls game :)\n'
          'You have five attempts\n'
          'Press "Q" four times at any point in the game to quit')

    remaining_tries = 5
    cows = 0
    bulls = 0

    while remaining_tries > 0:
        # generate a random number
        randNum = str(random.randint(1000, 9999))
        usr_guess = input('\nGuess a 4-digit number.\n')

        # Length of user's guess should be 4
        while len(usr_guess) != 4:
            print('Invalid input')
            usr_guess = input('Guess a 4-digit number.\n')

        if usr_guess == randNum:
            print('Yayyy!!! You guessed it.\n'
                  f'The secret number is {randNum}.'
                  'You win!!')
            print(f'Bulls: {bulls}\n'
                  f'Cows: {cows}\n')
            break

        # compare user's guess to random number
        # Bulls block
        elif usr_guess[0] == randNum[0]:
            bulls += 1
        elif usr_guess[1] == randNum[1]:
            bulls += 1
        elif usr_guess[2] == randNum[2]:
            bulls += 1
        elif usr_guess[3] == randNum[3]:
            bulls += 1

        # Cows block
        elif usr_guess[0] in randNum and usr_guess[0] != randNum[0]:
            cows += 1
        elif usr_guess[1] in randNum and usr_guess[1] != randNum[1]:
            cows += 1
        elif usr_guess[2] in randNum and usr_guess[2] != randNum[2]:
            cows += 1
        elif usr_guess[3] in randNum and usr_guess[3] != randNum[3]:
            cows += 1

        # Quit block
        elif usr_guess == "qqqq" or usr_guess == "QQQQ":
            print('Winners never quit but you just did :(')
            print(f'Bulls: {bulls}\n'
                  f'Cows: {cows}\n'
                  f'Game Over!!!')
            break

        # No correct guess
        else:
            print('Oops!!! You had nothing for this try\n'
                  'Try again\n')
            remaining_tries -= 1

        print(f'The secret number is {randNum}\n')
        print(f'Bulls: {bulls}\n'
              f'Cows: {cows}\n'
              f'Remaining attempts: {remaining_tries}')

    while remaining_tries == 0:
        print('You have exhausted all your attempts\n'
              'Game Over!!!')
        break

print(cows_and_bulls())
