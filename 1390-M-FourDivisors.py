from typing import DefaultDict, List
import collections
import math

def sumFourDivisors(arr: List[int]):
    res = 0
    for n in arr:
        divisors = set()
        for d in range(1, math.floor(math.sqrt(n) + 1)):
            if n % d == 0:
                divisors.add(d)
                divisors.add(n // d)
        if len(divisors) == 4:
            res += sum(divisors)
    return res


print(sumFourDivisors([21,21]))