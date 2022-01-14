from typing import List
import collections

def maxDistance(nums1: List[int], nums2: List[int]) -> int:
    len1, len2 = len(nums1), len(nums2)
    ans = 0
    i = j = 0
    while i < len1 and j < len2:
        if nums1[i] > nums2[j]:
            i+=1
        else:
            ans = max(ans, j - i)
            j+=1
    return ans

print(maxDistance([55,30,5,4,2],[100,20,10,10,5]))
print(maxDistance([2,2,2],[10,10,1]))
print(maxDistance([30,29,19,5],[25,25,25,25,25]))
print(maxDistance([5,4],[3,2]))
print(maxDistance([100000,99999,99998,99997,99996,99995,99994,99994,99993,99991,99987,99984,99982,99981,99981,99980,99979,99978,99978,99976,99975,99975,99974,99968,99966,99965,99963,99963,99961,99961,99961,99960,99960,99959,99958,99957,99957,99946,99945,99943,99942,99942,99941,99940,99939,99939,99938,99936,99930,99925,99925,99923,99922,99919,99919,99918,99916,99915,99913,99911,99911,99909,99909,99908,99907,99906,99906,99904,99901,99901,99895,99895,99891,99891,99890,99890,99888,99886,99885,99884,99884,99884,99883,99882,99881,99880,99879,99879,99877,99877,99871,99869,99869,99865,99865,99862,99861,99859,99859,99859,99858,99856,99854,99854,99853,99851,99850,99848,99843,99840,99835,99834,99832,99829,99824,99823,99822,99819,99818,99814,99811,99811,99806,99803,99801,99799,99798,99797,99797,99797,99794,99794,99792,99790,99790,99789,99786,99786,99784,99784,99782,99781,99781,99776,99776,99775,99775,99774,99774,99772,99772,99771,99771,99771,99766,99766,99765,99762,99758,99758,99757,99754,99753,99752,99748,99748,99], [100000,99999,99999,99999,99997,99996,99996,99995,99995,99995,99995,99995,99995,99995,99994,99994,99994,99993,99993,99992,99992,99991,99991,99990,99990,99990,99990,99990,99989,99989,99989,99989,99989,99989,99988,99988,99988,99988,99988,99987,99986,99986,99986,99985,99985,99985,99985,99985,99984,99984,99984,99983,99982,99982,99982,99982,99982,99982,99981,99981,99981,99981,99981,99981,99980,99980,99980,99978,99978,99978,99978,99977,99977,99977,99977,99977,99976,99976,99976,99976,99976,99975,99975,99975,99974,99974,99973,99973,99972,99972,99972,99972,99972,99972,99972,99971,99971,99971,99971,99971,99971,99970,99970,99970,99969,99969,99968,99968,99968,99968,99968,99967,99967,99967,99967,99967,99967,99966,99966,99966,99965,99965,99965,99965,99964,99963,99963,99963,99962,99962,99962,99962,99962,99962,99961,99961,99961,99959,99959,99959,99959,99959,99959,99959,99959,99959,99957,99956,99956,99955,99955,99955,99955,99954,99954,99954,99953,99953,99952,99952,99952,99950,99950,99950,99950,99950,99]))