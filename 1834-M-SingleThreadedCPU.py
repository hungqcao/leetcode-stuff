from typing import List
import collections
import math
import itertools
import heapq

def getOrder(tasks: List[List[int]]) -> List[int]:
    tasks = [[task[0], task[1], idx] for idx, task in enumerate(tasks)]
    tasks = sorted(tasks, key=lambda x: (x[0], x[1], x[2]))
    ans = []
    heap = []
    idx = 1
    curEnqueueTime, curProcessingTime, curIdx = tasks[0]
    ans.append(curIdx)
    endTime = curEnqueueTime + curProcessingTime
    while idx < len(tasks):
        curEnqueueTime, curProcessingTime, curIdx = tasks[idx]    
        
        if curEnqueueTime <= endTime:
            heapq.heappush(heap, (curProcessingTime, curIdx, curEnqueueTime))
            idx+=1
        elif not heap:
            endTime = curEnqueueTime + curProcessingTime
            ans.append(curIdx)
            idx+=1
        else:
            curProcessingTime, curIdx, curEnqueueTime = heapq.heappop(heap)
            endTime = endTime + curProcessingTime
            ans.append(curIdx)

        
    while heap:
        ans.append(heapq.heappop(heap)[1])
        
    return ans
    
print(getOrder([[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]))
print(getOrder([[1000000000,1000000000]]))
print(getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
print(getOrder([[1,2],[2,4],[3,2],[4,1]]))
print(getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]))