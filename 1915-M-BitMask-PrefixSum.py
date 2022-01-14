from typing import List
import collections
import math

def wonderfulSubstrings(word: str) -> int:
    count = [0] * 1024
    count[0] =  1
    mask = 0
    ans = 0
    for c in word:
        mask ^= 1 << (ord(c) - ord('a'))
        ans += count[mask]
        for i in range(10):
            prev = mask ^ (1 << i)
            ans += count[prev]
        count[mask] += 1
    return ans



print(wonderfulSubstrings('aba'))
print(wonderfulSubstrings('aabb'))
print(wonderfulSubstrings('he'))