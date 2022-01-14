from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = [first]
        for e in encoded:
            first ^= e
            ret.append(first)
        return ret

sol = Solution()
print(sol.decode([1,2,3], 1))
print(sol.decode([6,2,7,3], 4))