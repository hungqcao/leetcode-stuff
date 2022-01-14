from typing import List
import collections
import math

def countSmaller(nums: List[int]) -> List[int]:
    ans, size, new_arr = [0 for i in range(len(nums))], len(nums), [(n, i) for i, n in enumerate(nums)]
    
    def mergeSort(start, end):
        if start == end: return
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)
        i = mid + 1
        for left in range(start,mid + 1):     
            cur = new_arr[left]
            if left > start:
                ans[cur[1]] += i - mid - 1
            while i <= end and cur[0] > new_arr[i][0]:
                ans[cur[1]] += 1
                i += 1
        new_arr[start:end+1] = sorted(new_arr[start:end+1], key=lambda x:x[0])
    mergeSort(0, size - 1)
    return ans
            
#print(countSmaller([5,2,6,1]))
#print(countSmaller([-1]))
#print(countSmaller([-1,-1]))
print(countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]))

def truncateSentence(self, s: str, k: int) -> str:
    return " ".join(list(s.split(' ')[:4]))