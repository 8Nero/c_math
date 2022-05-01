import random, pylab
vals = [1, 200] #guarantee that values will range from 1 to 200
for i in range(1000):
    num1 = random.choice(range(1, 100))
    num2 = random.choice(range(1, 100))
    vals.append(num1+num2)

pylab.hist(vals, bins = 10)
pylab.show()
