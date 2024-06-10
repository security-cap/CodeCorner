import random, sys

print('ROCK, PAPER, SCISSER')
print()

# this veriable keep track of the number of wins, lose, ties.
win = 0
lose = 0
ties = 0 

while True: # the main game loop
        print('%s Win %s Losses, %s Ties' %(win, lose, ties))
        while True: # player input loop
                print('Enter your move: (r)ock (p)aper (s)cissers or (q)uit')
                playermove = input()
                if playermove == 'q':
                        sys.exit()
                if playermove == 'r' or playermove == 'p' or playermove == 's':
                        break #output of the player input loop
                print('type one of r, p, s, or q')
        
        #display what the player chose
        if playermove == 'r':
                print('ROCK versus....')
        elif playermove == 'p':
                print('PAPER versus....')
        elif playermove == 's':
                print('SCISSORS versus....')
        
        #display what the computer chose
        randomNumber = random.randint(1,3)
        
        if randomNumber == 1:
                cmtmove = 'r'
                print('Rock')
        elif randomNumber == 2:
                cmtmove = 'p'
                print('PAPER')
        elif randomNumber == 3:
                cmtmove = 's'

        #display and record the win/lose/tie:
        if playermove == cmtmove:
                print('It is a tie!')
                ties = ties + 1
        elif playermove == 'r' and cmtmove == 's':
                print('you win!')
                win = win + 1
        elif playermove == 'p' and cmtmove == 'r':
                print('You win!')
                win = win + 1
        elif playermove == 's' and cmtmove == 'p':
                print('you win!')
                win= win + 1
        elif playermove == 'r' and cmtmove == 'p':
                print('you loss!')
                lose = lose + 1
        elif playermove == 'p' and cmtmove == 's':
                print('you lose!')
                lose = lose +1
        elif playermove == 's' and cmtmove =='r':
                print('you lose!')
                lose = lose + 1