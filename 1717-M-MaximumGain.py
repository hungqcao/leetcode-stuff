from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

def maximumGain(s: str, x: int, y: int):
    def check(a,b,x,s):
        stack, count = [], 0
        for i in s:
            if i == a and stack and stack[-1] == b:
                stack.pop()
                count += x
            else:stack.append(i)
        return count,stack
    count = 0
    if y > x:
        count, s = check('a','b',y,s) 
        count += check('b','a',x,s)[0]
    else:
        count, s = check('b','a',x,s) 
        count += check('a','b',y,s)[0]
    return (count)

def maximumGain2(s: str, x: int, y: int) -> int:
    point, stack = 0,[]
    greater_pair = 'ab' if x > y else 'ba'
    smaller = "".join(greater_pair[::-1])
    max_val, min_val = max(x,y), min(x, y)
    for c in s:
        print(stack)
        if c == greater_pair[1]:
            if stack and stack[-1] == greater_pair[0]:
                point += max_val
                stack.pop()
            else:
                stack.append(c)
        elif c == greater_pair[0]:
            stack.append(c)
        elif stack:
            cur = stack.pop(0)
            tmp_stack = [cur]
            while stack:
                tmp = stack.pop(0)                 
                if tmp_stack and tmp_stack[-1]:
                    cur = tmp_stack[-1]                    
                    cur+=tmp                
                    if cur == greater_pair:
                        point += max_val
                        tmp_stack.pop(0)
                    elif cur == smaller:
                        point += min_val
                        tmp_stack.pop(0)
                    else:
                        tmp_stack.append(tmp)
                else:
                    tmp_stack.append(tmp)
        print(point)
    cur = stack.pop(0) if stack else ''
    tmp_stack = [cur]
    while stack:
        tmp = stack.pop(0)                 
        if tmp_stack and tmp_stack[-1]:
            cur = tmp_stack[-1]                    
            cur+=tmp                
            if cur == greater_pair:
                point += max_val
                tmp_stack.pop(0)
            elif cur == smaller:
                point += min_val
                tmp_stack.pop(0)
            else:
                tmp_stack.append(tmp)
        else:
            tmp_stack.append(tmp)

    return point

print(maximumGain('aabbaaxybbaabb', 5, 4))
#maximumGain("aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha",1926,4320)