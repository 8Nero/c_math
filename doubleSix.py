import random

def diceDoubleRoll(numRolls):
    outcomes = (1,2,3,4,5,6)
    result = []
    doubleSix = 0
    for d in range(numRolls):
        x = random.choice(outcomes)
        result.append(x)
        y = random.choice(outcomes)
        result.append(y)

        if x == 6 and y == 6:
            doubleSix += 1

    return doubleSix

def simRoll(numTrials, numRolls):
    doubleSixs = 0
    for _ in range(numTrials):
        if diceDoubleRoll(numRolls):
            doubleSixs += 1
    print("Number of Trials: ", numTrials)
    print("Probability of double six, based on the data\n", doubleSixs/numTrials)

simRoll(100000, 24)
