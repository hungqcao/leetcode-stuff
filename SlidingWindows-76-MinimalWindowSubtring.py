from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = end = 0
        counter = collections.defaultdict(int)
        for c in t:
            counter[c] += 1
        count = len(counter)
        res = s
        while end < len(s):
            if s[end] in counter:
                counter[s[end]] -= 1
                if counter[s[end]] == 0:
                    count -= 1
            end += 1
            
            while count == 0:
                if s[start] in counter:
                    counter[s[start]] += 1
                    if counter[s[start]] > 0:
                        count += 1
                if len(res) > end - start:
                    res = s[start:end]
                start += 1
        return res



        
sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))