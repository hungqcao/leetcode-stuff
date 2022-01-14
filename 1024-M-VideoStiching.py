from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

def videoStitching(clips: List[List[int]], time: int) -> int:
    jumps =[0 for i in range(time)]
    # if not jumps:
    #     return 0
    for clip in clips:
        if clip[0] >= time: continue
        right = clip[1] if clip[1] <= time else time
        jumps[clip[0]] = max(jumps[clip[0]], right)
    print(jumps)
    left = right = steps = 0
    while right < len(jumps):
        left, right = right, max([jumps[i] for i in range(left,right+1)])
        print(f"{left} {right}")
        if left == right or left >= right: return -1
        steps += 1
    return steps

#print(videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))
#print(videoStitching([[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]], 5))
#print(videoStitching([[2,4]], 0))
print(videoStitching([[4,28],[8,23],[11,39],[6,25],[0,15],[3,27],[6,39],[4,27]], 60))