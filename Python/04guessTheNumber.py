# this is the guessing number game
import random

guessNumber = random.randint(1,20)
print('i am thinking of a number between 1 to 20')


# asking playter to gacing thair number 6 times
for guessTake in range(1,7):

        print('Guess your number')
        guess = int(input())

        if guessNumber > guess:
                print('you are to low incress plese')
        elif guessNumber < guess:
                print('you are to high decress plese')
        else:
                break # this condition is the correct guess
if guessNumber == guess:
        print('Good job! You guess my number in ' + str(guess) +' guess. and you guess it ' + str(guessTake) + ' Time' )
else:
        print('Nope! The number i was thinking of was '+ str(guessNumber))
