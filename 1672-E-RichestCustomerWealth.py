from typing import List
import collections
import math

def maximumWealth(accounts: List[List[int]]) -> int:
    res = 0
    for bank in accounts:
        res = max(res, sum(bank))
    return res



print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))