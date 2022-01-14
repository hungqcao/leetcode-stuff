from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json
import functools

class Solution:

    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) 
            res |= (n & 1)
            n >>= 1
            #res <<= 1
            # res = (res << 1) + (n & 1)
            # n >>= 1
        return res

sol = Solution()
print(sol.reverseBits(int("100", 2)))
"111001011110000010100101000000"
"1110010111100000101001010000000"
"00000010100101000001111010011100"