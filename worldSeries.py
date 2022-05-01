import random, pylab

def playSeries(numGames, teamProb):
    numWon = 0
    for game in range(numGames):
        if random.random() < teamProb:
            numWon += 1
    return (numWon > numGames//2)

def simSeries(numSeries):
    prob = 0.5
    fracWon = []
    probs = []
    while prob <= 1.0:
        seriesWon = 0.0
        for i in range(numSeries):
            if playSeries(7, prob):
                seriesWon += 1
        fracWon.append(seriesWon/numSeries)
        probs.append(prob)
        prob += 0.01

    pylab.plot(probs, fracWon, linewidth = 2)
    pylab.xlabel('Probability of Winning a Game')
    pylab.ylabel('Probability of Winning a Series')
    pylab.axhline(0.95)
    pylab.ylim(0.5, 1.1)
    pylab.title(str(numSeries) + ' Seven-Game Series')
    pylab.show()

simSeries(100000)
