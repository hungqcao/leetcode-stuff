
from typing import List

def canArrange(arr: List[int], k: int) -> int:
    count = [0 for i in range(k)]
    for a in arr:
        count[a % k] += 1
    expected = len(arr) // 2
    for i in range(0, len(count)):
        if (count[i] > 0):
            if i != (k-i)%k:
                numPairs = min(count[i], count[(k-i)%k])
                expected -= numPairs
                count[i] -= numPairs
                count[(k-i)%k] -= numPairs
            elif count[i] > 1:
                expected -= (count[i] // 2)
                count[i] -= (count[i] // 2) * 2



    print(expected)
    print(count)
    return expected == 0 

print(canArrange([1,2,3,4,5,10,6,7,8,9], 5))
print(canArrange([1,2,3,4,5,6], 7))
print(canArrange([1,2,3,4,5,6], 10))
print(canArrange([-10, 10], 2))
print(canArrange([-1,1,-2,2,-3,3,-4,4], 3))
print(canArrange([3,8,17,2,5,6], 10))

