import random
import pylab

def stdDev(X):
    size = len(X)
    mu = float(sum(X))/size
    tot = 0

    for x in X:
        tot += (x - mu)**2

    return (tot/size)**0.5

def CV(X):
    mu = sum(X)/float(len(X))
    try:
        return stdDev(X)/mu
    except ZeroDivisionError:
        return float('nan')


def makePlot(xVals, yVals, title, xLabel, yLabel, style,
             logX=False, logY=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()
    pylab.show()

def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.random() < 0.5:
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)


def flipPlot(minExp, maxExp, numTrials):
    """Plots results of 2**minExp to 2**maxExp coin flips"""

    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [],[],[],[]
    ratiosCVs, diffsCVs = [], []
    xAxis = []

    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)

    for numFlips in xAxis:
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))

        ratiosMeans.append(sum(ratios)/float(numTrials))
        diffsMeans.append(sum(diffs)/float(numTrials))
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))


    numTrialsString = '(' + str(numTrials) + ' Trials)'
    title = 'Mean Heads/Tails Ratios ' + numTrialsString
    makePlot(xAxis, ratiosMeans, title,
             'Number of Flips', 'Mean Heads/Tails', 'bo', logX = True)
    title = 'SD Heads/Tails Ratios ' + numTrialsString
    makePlot(xAxis, ratiosSDs, title,
             'Number of Flips', 'Standard Deviation', 'bo',
             logX = True, logY = True)

random.seed(0)
flipPlot(4,20, 20)


