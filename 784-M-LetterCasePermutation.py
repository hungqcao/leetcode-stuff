from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

def letterCasePermutation(s: str) -> List[str]:
    queue = [(0,s)]
    res = set()
    while queue:
        size = len(queue)
        for i in range(size):
            idx, tmp = queue.pop(0)
            while idx < len(s) and not tmp[idx].isalpha():
                idx+=1
            if idx < len(s) and tmp[idx].isalpha():
                new_s_1 = tmp[:idx] + tmp[idx].upper() + tmp[idx+1:]
                new_s_2 = tmp[:idx] + tmp[idx].lower() + tmp[idx+1:]
                queue.append((idx+1, new_s_1))
                queue.append((idx+1, new_s_2))
            if idx >= len(s):
                res.add(tmp)
    return list(res)

print(letterCasePermutation("a1b2"))
print(letterCasePermutation("3z4"))
print(letterCasePermutation("12345"))
print(letterCasePermutation("0"))
print(letterCasePermutation("aaaaaaaaaaaaaa"))