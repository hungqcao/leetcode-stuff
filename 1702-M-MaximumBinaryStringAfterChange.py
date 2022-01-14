from typing import List
import collections
import math

def maximumBinaryString(s: str):
    if '0' not in s: return s
    k, n = s.count('1', s.find('0')), len(s)
    return '1' * (n-k-1) + '0' + '1'*k




print(maximumBinaryString('000110'))