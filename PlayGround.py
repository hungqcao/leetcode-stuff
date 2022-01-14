from typing import List
import math
import sys
import os
import collections
from common import create2DArray, __location__
import json
import functools
import heapq
def solution(A, B):
    small, big = min(A, B), max(A, B)
    left, right = 0, big
    while left < right:
        mid = (left + right) // 2

        if (mid >= small and mid * 4 <= big) or (mid < small and (mid * 3 <= big) or (mid * 2) <= small):
            left = mid + 1
        else:
            right = mid
    return left - 1

def solution2(A, B):
    # write your code in Python 3.6
    small, big = min(A, B), max(A, B)
    left, right = 0, big + 1
    while right - left > 1:
        mid = (left + right) // 2
        if (mid >= small and mid * 4 <= big) or (mid < small and (mid * 3 <= big) or (mid * 2) <= small):
            left = mid
        else:
            right = mid
    return left 

number_dict = {
    1: ['_'],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'], 
    5: ['J','K','L']       
}

@functools.lru_cache(None)
def dfs(cur_number, remain_digit):
    #print(f'{cur_number} {remain_digit}')
    if remain_digit == 0:
        print(cur_number)
        return
    
    for number in range(1, 10): # 1->9
        if number in number_dict:
            for character in number_dict[number]:
                dfs(cur_number + str(character), remain_digit - 1, number_dict)
        

def method():

    for first in number_dict[4]:
        for second in number_dict[2]:
            for third in number_dict[5]:
                dfs(first+second+third, 7, number_dict)


def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    boxes = sorted(boxTypes, key=lambda x: -x[1])
    res = 0
    num_box = 0
    for box, units in boxes:
        for i in range(box, 0, -1):
            if num_box + i <= truckSize:
                res += (units * i)
                num_box += i
                break
    print(res)
    return res

assert maximumUnits([[1,3],[2,2],[3,1]], 4) == 8
assert maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10) == 91

# print(solution(10, 21))
# print(solution(13, 11))
# print(solution(2, 1))
# print(solution(1, 8))
# print(solution(3, 16))