from typing import List
import collections
import math
import itertools

def threeSumMulti(arr: List[int], target: int) -> int:
    count = 0
    count_maps = collections.Counter(arr)

    for i, j in itertools.combinations_with_replacement(count_maps, 2):
        k = target - i - j
        if k > i and k > j and i != j:
            count += count_maps[k]*count_maps[i]*count_maps[j]
        elif i == j == k:
            count += math.factorial(count_maps[i]) / (math.factorial(count_maps[i] - 3)) / 6
        elif i == j != k:
            count += count_maps[i] * ((count_maps[i] - 1) / 2)*count_maps[k]

    return count % (10**9 + 7)
            


print(threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))
