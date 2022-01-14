from typing import List
import collections
import math
import heapq

def getSkyline2(buildings: List[List[int]]):
    ans, cords, heap = [], [], [0]
    for b in buildings:
        cords.append((b[0], b[2], True))
        cords.append((b[1], b[2], False))
    cords = sorted(cords, key=lambda x: (x[0], -x[1]))    

    print(cords)
    for cord in cords:
        if cord[2]:
            #start
            before = heap[0]
            heapq.heappush(heap, -cord[1])
            after = heap[0]
            if before != after:
                ans.append([cord[0], -after])

        else:
            #end
            before = heap[0]
            heap.remove(-cord[1])
            heapq.heapify(heap)
            after = heap[0]
            if before != after:
                ans.append([cord[0], -after])
    return ans

def getSkyline(buildings):
    def addsky(pos, hei):
        if sky[-1][1] != hei:
            sky.append([pos, hei])

    sky = [[-1,0]]
    
    # possible corner positions
    position = set([b[0] for b in buildings] + [b[1] for b in buildings])
    
    # live buildings
    live = []
    
    i = 0
        
    for t in sorted(position):
        
        # add the new buildings whose left side is lefter than position t
        while i < len(buildings) and buildings[i][0] <= t:
            heapq.heappush(live, (-buildings[i][2], buildings[i][1]))
            i += 1
            
        # remove the past buildings whose right side is lefter than position t
        while live and live[0][1] <= t:
            heapq.heappop(live)
        
        # pick the highest existing building at this moment
        h = -live[0][0] if live else 0
        addsky(t, h)

    return sky[1:]            
print(getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))

set().intersection(set()).