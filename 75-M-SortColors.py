from typing import List

def sortColors(nums: List[int]) -> None:
    head, cur, tail = 0, 0, len(nums) - 1
    def swap(x, y):
        tmp = nums[x]
        nums[x] = nums[y]
        nums[y] = tmp
    while cur <= tail:
        print(nums)
        if nums[cur] == 0:
            swap(cur, head)
            head += 1
            cur += 1
        elif nums[cur] == 2:
            swap(cur, tail)
            tail -= 1
        else:
            cur += 1

#sortColors([1, 0, 1])
sortColors([2, 0, 1])
#sortColors([2, 1, 2])
#sortColors([0, 1, 0])
#sortColors([2,0,2,1,1,0])