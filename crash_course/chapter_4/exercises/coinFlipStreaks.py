import random
numberOfStreaks = 0


for experiments in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flipList = []
    for x in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            flipList.append('H')
        else:
            flipList.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 0
    for x in range(len(flipList)):

        if flipList[x] == flipList[x-1]:
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1   
            streak = 0  

print(numberOfStreaks)

print('Chance of streak: %s%%' % (numberOfStreaks / 100))