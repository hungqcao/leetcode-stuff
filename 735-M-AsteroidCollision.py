from typing import List
import collections
import math
import itertools

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    for num in asteroids:
        if num > 0: stack.append(num)
        else:
            while stack and stack[-1] > 0 and stack[-1] < abs(num):
                stack.pop()
            if not stack and stack[-1] < 0: stack.append(num)
            elif stack[-1] == -num: stack.pop()

    return stack


#print(asteroidCollision([5, 10, -5]))
#print(asteroidCollision([8, -8]))
print(asteroidCollision([10, 2, -5]))
#print(asteroidCollision([-2, -1, 1, 2]))
