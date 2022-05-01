import pylab, random, statistics

class Location(object):
    def __init__(self, x, y):
        """
        x and y are floats
        """
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """
        deltaX and deltaY are floats
        """
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        deltaX = self.x - other.x
        deltaY = self.y - other.y
        return (deltaX**2 + deltaY**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate Drunk!')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #Use move method from Location class to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk(object):
    def __init(self, name = None):
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Just a Drunkard'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-1.0),(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-2.0), (1.0,0.0), (-1.0,0.0)]
        return random.choice(stepChoices)

class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0,0.0), (-1.0,0.0)]
        return random.choice(stepChoices)


class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


def walk(f, d, numSteps):
    """
     f: a Field
     d: a Drunk in f
     numSteps: an int >= 0
     """
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)

    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    Homer = dClass()
    origin = Location(0.0, 0.0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(walk(f, Homer, numSteps))
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        mu = sum(distances)/len(distances)

        print(dClass.__name__, 'random walk of', numSteps, 'steps')

        print(' Mean =', mu,\
              'CV =', statistics.pstdev(distances, mu)/mu)

        print(' Max=', max(distances), 'Min =', min(distances))

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    cvDistances = []
    for numSteps in walkLengths:
        print("Starting simulation of", numSteps, "steps")
        trials = simWalks(numSteps, numTrials, dClass)
        mu = sum(trials)/float(len(trials))
        meanDistances.append(mu)
        cvDistances.append(statistics.pstdev(trials, mu)/mu)
    return (meanDistances, cvDistances)

def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('b-', 'r:', 'm-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print("Starting simulation of", dClass.__name__)
        means, cvs = simDrunk(numTrials, dClass, walkLengths)
        cvMean = sum(cvs)/float(len(cvs))
        pylab.plot(walkLengths, means, curStyle,
                   label = dClass.__name__ + '(CV = ' + str(round(cvMean, 4)) + ')')

       # drunkTest(walkLengths, numTrials, dClass)
    pylab.title('Mean Distance from Origin (' + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()

def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    origin = Location(0,0)
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, origin)
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('b+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for l in locs:
            xVals.append(l.getX())
            yVals.append(l.getY())
        meanX = sum(xVals)/float(len(xVals))
        meanY = sum(yVals)/float(len(yVals))
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                   label = dClass.__name__ + ' Mean loc. = <'
                   + str(meanX) + ',' + str(meanY) + '>')
    pylab.title('Location at End of Walks ('
                + str(numSteps) + ' steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'lower left', numpoints = 1)
    pylab.show()

def traceWalk(drunkKinds, numSteps):
    styleChoice = styleIterator(('b+', 'r^', 'mo'))
    f = oddField(1000, 100, 200)
    for dClass in drunkKinds:
        d = dClass()
        f.addDrunk(d, Location(0,0))
        locs = []
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))

        xVals = []
        yVals = []
        for l in locs:
            xVals.append(l.getX())
            yVals.append(l.getY())
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                   label = dClass.__name__)
    pylab.title('Spots Visited on Walk ('
                + str(numSteps) + ' steps)')
    pylab.ylabel('Steps North/South of Origin')
    pylab.xlabel('Steps East/West of Origin')
    pylab.legend(loc = 'best')
    pylab.show()

class oddField(Field):
    def __init__(self, numHoles, xRange, yRange):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormholes[(x, y)] = newLoc

        def moveDrunk(self, drunk):
            Field.moveDrunk(self, drunk)
            x = self.drunks[drunk].getX()
            y = self.drunks[drunk].getY()
            if (x, y) in self.wormholes:
                self.drunks[drunk] = self.wormholes[(x,y)]


drunkKinds = (UsualDrunk, ColdDrunk, EWDrunk)
walkLengths = (10, 100, 1000, 10000, 100000)

#simAll(drunkKinds, walkLengths, 100)
#plotLocs(drunkKinds, 100, 200)
traceWalk(drunkKinds, 500)











