from typing import List
import collections

def getSmallestString(n:int, k:int) -> str:
    k -= n
    string = chr((k + k//25)%26 + 97) + k//25 * "z"
    while len(string) > n:
        string = string[1:]
    return f"{string:a>{n}}"

def getSmallestString2(n: int, k: int) -> str:
    res, cur_sum = '', 0
    for i in range(1,n+1):
        for c in range(1,27)[::-1]:
            if cur_sum == k:
                return res
            if k - (c + cur_sum) >= n - i:
                cur_sum += c
                res += chr(c + 96)
                break

    return res[::-1]


print(getSmallestString(5,73))
print(getSmallestString(3,27))