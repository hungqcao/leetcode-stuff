from typing import List
import collections
import math

def maximumGap(num):
    if len(num) < 2 or min(num) == max(num):
        return 0
    a, b = min(num), max(num)
    size = math.ceil((b-a)/(len(num)-1))
    bucket = [[None, None] for _ in range((b-a)//size+1)]
    for n in num:
        b = bucket[(n - a)//size]
        b[0] = n if b[0] is None else min(b[0], n)
        b[1] = n if b[1] is None else max(b[1], n)
    print(bucket)
    bucket = [b for b in bucket if b[0] is not None]
    return max(bucket[i][0] - bucket[i-1][1] for i in range(1, len(bucket)))



print(maximumGap([8,1,9,4,5,10,43]))