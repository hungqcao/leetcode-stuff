from typing import List

def minSwap(A: List[int], B: List[int]) -> int:
    size = len(A), prev_swap, prev_not_swap =  1, 0
    for i in range(1, size):
        areBothSelfIncreasing = A[i - 1] < A[i] and B[i - 1] < B[i]
        areInterchangeInCreasing = A[i - 1] < B[i] and B[i-1] < A[i]
        if areBothSelfIncreasing and areInterchangeInCreasing:
            prev_swap = min(prev_not_swap, prev_swap) + 1
            prev_not_swap = min(prev_not_swap, prev_swap)
        elif areBothSelfIncreasing:
            prev_swap+=1
        else:
            prev_swap = prev_not_swap + 1
            prev_not_swap = prev_swap

    return min(prev_swap, prev_not_swap)

    
[3,3,8,9,10]
[1,7,4,6,8]
1