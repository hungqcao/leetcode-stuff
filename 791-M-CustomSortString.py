from typing import Counter, List
import collections
import math
import sys
from common import create2DArray

def customSortString(order: str, str: str) -> str:
    res, dict = '', Counter(str)
    for c in order:
        num = dict[c]
        res += c * num
        dict[c] = 0
    
    for c in dict:
        if dict[c] > 0:
            res += c * dict[c]

    return res



#maxHeight([[50,45,20],[95,37,53],[45,23,12]])
print(customSortString("cba", 'abcd'))