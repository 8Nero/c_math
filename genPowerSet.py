def getBinaryRep(n, numDigits):
    result = ''

    while n > 0:
        result = str(n%2) + result
        n = n//2

    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result

def genPowerset(L):

    powerset = []
    for i in range(0, 2**len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset

test1 = genPowerset(['a','b','c'])
test2 = genPowerset(['a','b','c','d'])
test3 = genPowerset(['a','b','c','d','e'])

print(f"Size:{len(test1)}\n", test1)
print(f"Size:{len(test2)}\n", test2)
print(f"Size:{len(test3)}\n", test3)


