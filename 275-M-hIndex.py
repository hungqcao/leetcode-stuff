from typing import List
import collections

def hIndex(citations: List[int]) -> int:
    left, right =  0, len(citations)
    while left < right:
        mid = (left + right) // 2
        h = len(citations) - mid
        if citations[mid] == h:
            return h
        elif citations[mid] > h:
            right = mid
        else:
            left = mid + 1
    return len(citations) - left


#print(hIndex([1]))
#print(hIndex([0]))
#print(hIndex([0,1,3,5,6]))
#print(hIndex([1,1,1,1]))
#print(hIndex([1,2,100]))

s = "is2 sentence4 This1 a3"
arr = s.split(" ")
arr.sort(key=lambda x:x[len(x) - 1])
print(" ".join(list(map(lambda x:x[0:len(x)-1], arr))))