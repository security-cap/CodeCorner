import random

def getAns(ansnum):
        if ansnum == 1:
                return 'it is certain'
        elif ansnum == 2:
                return 'It is decidedly so'
        elif ansnum == 3:
                return 'Yes'
        elif ansnum == 4:
                return 'Replay hazy try again'
        elif ansnum == 5:
                return 'Ask again leter'
        elif ansnum == 6:
                return 'Concentrated and ask again'
        elif ansnum == 7:
                return 'My replay is no'
        elif ansnum == 8:
                return 'very doutfull'

# r = random.randint(1,9)
# fortun = getAns(r)
# print(fortun)

print(getAns(random.randint(1,9))) #to of there line of code and this line of code are same