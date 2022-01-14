from typing import List
import collections
import math

def simplifiedFractions(n: int) -> List[str]:
    if (n == 1):
        return []
    res = []
    def findGCD(a, b):
        if (b == 0):
            return a
        return findGCD(b, a % b)
    for i in range(2, n + 1):
        for j in range(1, i):
            if (j != 1 and findGCD(i, j) == 1):
                res.append(f"{j}/{i}")
            elif (j == 1):
                res.append(f"{j}/{i}")
    return res



print(simplifiedFractions(1))
print(simplifiedFractions(2))
print(simplifiedFractions(3))
print(simplifiedFractions(4))
print(simplifiedFractions(6))