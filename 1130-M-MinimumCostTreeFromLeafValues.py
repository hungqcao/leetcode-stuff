from typing import List
import collections

def mctFromLeafValues(arr: List[int]) -> int:
    res = 0
    stack = [float('inf')]
    for a in arr:
        while stack[-1] <= a:
            mid = stack.pop()
            res += mid * min(a, stack[-1])
        stack.append(a)
    while len(stack) > 2:
        res += stack.pop() * stack[-1]
    return res




print(mctFromLeafValues([6,2,4,1,5]))