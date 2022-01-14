from typing import List
import collections
import math

def findMinMoves(machines: List[int]) -> int:
    total, size = sum(machines), len(machines)
    if total % size != 0: return -1
    left_sum = [0 for _ in range(size)]
    for i in range(1, size):
        left_sum[i] = left_sum[i-1] + machines[i - 1]
    right_sum = [0 for _ in range(size)]
    for i in range(size - 2, -1, - 1):
        right_sum[i] = right_sum[i + 1] + machines[i + 1]
    each = total // size
    res = 0
    for i in range(size):
        expected_left = each * i
        expected_right = each * (size - i - 1)
        left = expected_left - left_sum[i] if expected_left > left_sum[i] else 0
        right = expected_right - right_sum[i] if expected_right > right_sum[i] else 0
        res = max(res, left + right)
    return res
            
print(findMinMoves([1, 0, 5]))
print(findMinMoves([0, 3, 0]))
print(findMinMoves([0, 2, 0]))