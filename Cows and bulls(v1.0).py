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
        rand_num = str(random.randint(1000, 9999))
        usr_guess = input('\nGuess a 4-digit number.\n')

        # Length of user's guess should be 4
        while len(usr_guess) != 4:
            print('Invalid input')
            usr_guess = input('Guess a 4-digit number.\n')

        if usr_guess == rand_num:
            print('Yayyy!!! You guessed it.\n'
                  f'The secret number is {rand_num}.'
                  'You win!!')
            print(f'Bulls: {bulls}\n'
                  f'Cows: {cows}\n')
            break

        # compare user's guess to random number
        # Bulls block
        elif usr_guess[0] == rand_num[0]:
            bulls += 1
        elif usr_guess[1] == rand_num[1]:
            bulls += 1
        elif usr_guess[2] == rand_num[2]:
            bulls += 1
        elif usr_guess[3] == rand_num[3]:
            bulls += 1

        # Cows block
        elif usr_guess[0] in rand_num and usr_guess[0] != rand_num[0]:
            cows += 1
        elif usr_guess[1] in rand_num and usr_guess[1] != rand_num[1]:
            cows += 1
        elif usr_guess[2] in rand_num and usr_guess[2] != rand_numrand_num[2]:
            cows += 1
        elif usr_guess[3] in rand_num and usr_guess[3] != rand_num[3]:
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

        print(f'The secret number is {rand_num}\n')
        print(f'Bulls: {bulls}\n'
              f'Cows: {cows}\n'
              f'Remaining attempts: {remaining_tries}')

    while remaining_tries == 0:
        print('You have exhausted all your attempts\n'
              'Game Over!!!')
        break

print(cows_and_bulls())
