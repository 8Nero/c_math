import pylab

def clear(n, p, steps):
    """
    Assumes n & steps positive ints, p a float
    n: the initial number of molecules
    p: the probability of a molecule being cleared
    steps: the length of the simulation
    """
    remainingMol = []
    for t in range(steps):
        remainingMol.append(n*((1-p)**t))

    print(remainingMol[:5])
    print(remainingMol[990:])
    pylab.plot(remainingMol)
    pylab.title('Clearance of Drug')
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.semilogy()
    pylab.show()

clear(1000, 0.01, 1000)

