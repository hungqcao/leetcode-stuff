from typing import List
import collections

def countNicePairs(nums: List[int]) -> int:
    def rev(num):
        res, tmp = 0, num
        while (tmp > 0):
            mod = tmp % 10
            tmp = tmp // 10
            res = res * 10 + mod
        return res
    res, mySet = 0, collections.Counter()
    for num in nums:
        reverted = rev(num)
        res += mySet[num - reverted]
        mySet[num - reverted] += 1
    return res % (10**9 + 7)


print(countNicePairs([42,11,1,97,123,4321,101,100,4320]))