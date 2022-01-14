from typing import List
import collections
import math
import sys
import os
from common import convertToTree
from common import create2DArray, __location__
import heapq
import functools
from common import TreeNode, ListNode
class Solution:

    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left, right = 0, len(plants) - 1

        refil = 0
        curA, curB = capacityA, capacityB
        while left < right:
            if plants[left] > curA:
                refil += 1
                curA = (capacityA - plants[left])
            else:
                curA -= plants[left]

            if plants[right] > curB:
                refil += 1
                curB = (capacityB - plants[right])
            else:
                curB -= plants[right]
            left += 1
            right -= 1
        if left == right:
            maxW = max(curA, curB)
            if maxW < plants[right]:
                refil += 1
        return refil

    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        #dp = [[(0, 0) for r in range(len(nums))] for r in range(len(nums))]
        for i in range(2, len(nums) + 1):
            for j in range(len(nums) - i + 1):
                #dp[i][j] = dp[i][j-1]                 
                c_min, c_max = float('inf'), float('-inf')
                for t in range(j, j+i):
                    c_min = min(c_min, nums[t])
                    c_max = max(c_max, nums[t])
                res += (c_max - c_min)
        return res

    def dfs(self, cur_pos, k, cur_fruits, visited):
        if cur_pos in self.dp:
            return self.dp[cur_pos]
        if k < 0:
            return cur_fruits
        if cur_pos < 0 or cur_pos > 2*10**5: return cur_fruits
        
        cur_fruits += self.graph[cur_pos]
        visited.add(cur_pos)
        res = cur_fruits
        for step in range(1, k + 1):
            if cur_pos + step not in visited and cur_pos + step in self.graph:
                res = max(res, self.dfs(cur_pos + step, k - step, cur_fruits, visited))
            if cur_pos - step not in visited and cur_pos - step in self.graph:
                res = max(res, self.dfs(cur_pos - step, k - step, cur_fruits, visited))
        visited.remove(cur_pos)
        self.res = max(self.res, res)
        self.dp[cur_pos] = max(self.dp[cur_pos], res)
        return res



    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        self.graph = collections.defaultdict(int)
        self.res = float('-inf')
        self.dp = collections.defaultdict(int)
        for fruit in fruits:
            self.graph[fruit[0]] = fruit[1]
        res = self.dfs(startPos, k, 0, set())
        return self.res
        

sol = Solution()
#print(sol.minimumRefill([2,2,3,3], 5, 5))
#print(sol.minimumRefill([2,2,3,3], 3, 4))
#print(sol.minimumRefill([5], 10, 8))
#print(sol.minimumRefill([1,2,4,4,5], 6, 5))
#print(sol.minimumRefill([2,2,5,2,2], 5, 5))

# print(sol.subArrayRanges([1,2,3]))
# print(sol.subArrayRanges([1,3,3]))
# print(sol.subArrayRanges([4,-2,-3,4,1]))
# print(sol.subArrayRanges([21782,52192,83011,-45569,47262,74307,43361,-11362,-69625,64854,-89635,76299,-20076,-17519,82582,13773,-53080,-58467,-49044,-23319,37070,-61324,58432,6151,-83621,86796,29552,-61085,-89960,9301,-19091,5972,-92773,-17590,93931,-26151,29282,29570,-91972,17837,93155,59251,-3746,75292,-14102,84430,29637,72875,-46638,86431,53153,69610,58962,-48085,-98440,89398,-75088,84050,-3812,97566,21922,72220,-92606,39334,96648,1958,3675,13018,-27418,90075,61340,84745,42920,41975,53852,-13038,-5143,-19135,22908,17945,93503,-96950,-49387,34151,-51116,72815,46077,6088,-94488,51215,87163,81639,97775,-1530,70288,-34280,-44242,8783,-31771,-82653,-16241,-18113,56491,67716,-17909,73144,-74666,-6719,-46416,39793,-14617,-82266,92626,6314,-58572,-51872,-12198,-34652,-75465,-9174,71872,86814,39067,-78433,65813,-63636,33867,14419,27952,24584,29844,42503,-94867,63241,66360,87590,-52402,81877,-30011,67834,87974,70425,9716,-12071,-20979,-37640,12470,-57230,90632,82207,98921,-65388,72437,58349,10815,43377,61616,64388,-68580,54143,-80172,68505,24506,-36908,52897,-66157,3174,16105,-19584,51529,43932,-80154,31777,-3641,-47139,-97906,-15438,73001,-38142,80280,-46889,-91939,-18302,43644,-7205,35358,99366,19939,-44863,88007,-9008,82230,-83368,56861,48376,-80199,25687,-86732,-74106,6330,-42530,17558,11655,52667,96640,88571,-41775,-32776,-95609,98382,-99400,72212,-45334,-12345,36121,2422,47700,-31558,-995,57977,18520,-62326,-59176,43656,66383,-62126,31231,-76009,-86524,-43170,37777,-66679,-44376,16755,-38099,10521,91552,-62286,10283,-42235,-53536,95948,41359,-64365,-88416,-47358,4691,-32981,95936,-9261,3409,-13035,95831,-94542,32849,-24405,-64924,42488,-83159,69512,-35576,31765,43584,74994,60659,-91373,-28332,-57720,-49052,-46980,69983,-78804,29607,15664,7733,10155,38653,-99692,74622,46474,18944,-42040,-92485,-93991,17254,9086,-59958,-81723,61714,-56053,-18360,-36923,-31339,56776,71954,40549,32360,84773,-64234,30613,94708,75882,1572,-68617,87431,-9454,-56639,20401,-94248,-73134,-20288,-55879,-54488,98235,48994,-64895,94333,-70227,-26586,-12171,-94518,82863,54730,-97239,62862,-87895,-51814,-92317,42612,-17080,57251,-63555,52130,-65631,81824,51856,12735,38832,-40259,-56471,-33516,47713,-33764,-82699,-60909,-10675,-8632,41340,67679,-17763,-88222,61663,-48018,-9541,72807,76292,-95929,-5318,-4033,-5113,59496,-33076,-45161,-78151,-64084,88556,-41459,-67957,-94837,-79015,-95264,74300,-5396,82684,66589,60883,15911,18095,57927,-40201,-85574,-46675,-68194,-37370,-41156,-42065,70474,-4880,-55049,28545,-99682,-8204,-81028,33610,-60927,27158,-92029,-53210,-58947,98784,-51389,93020,-26835,-65949,97177,-739,94165,-28424,20352,-51850,-21745,-17595,-82240,-60114,75334,-11926,-54629,-34684,16166,-38493,-99889,80622,64726,42880,89522,48336,42644,-83896,92630,46555,-9519,-85330,22023,46377,62108,78236,-60885,-86202,-81008,-68412,-81475,22200,60567,-51882,-87692,-88802,45812,-35399,-15926,3025,43507,41258,74998,9190,48146,-95918,-65944,-67331,50489,9979,-23167,71612,13638,55333,-57173,-93041,93933,-56147,-25154,-16987,-68433,24074,-66844,80570,-25636,52980,-45489,78635,-48938,24049,-62176,59476,-9463,65958,41022,43829,23046,64250,-49363,-7213,-71123,-80478,2348,95458,87106,87367,5153,-31352,-4057,90358,81126,85050,59170,39831,-5321,60828,-11122,22856,-86206,-93792,-97495,8421,75662,66585,-61411,-19763,47109,-58175,-20297,-3566,80969,84381,-70769,-58542,-95311,-44196,10978,64936,-82311,59709,-77343,67348,42781,-6081,48218,-9441,-21798,61723,-33287,22520,63470,-35337,-921,-75703,77777,30199,-93336,36688,50494,88350,-36747,25507,-78934,-61779,-14182,3126,-95561,73706,-22657,-80293,31390,-85141,17557,-72136,-61701,-63838,44948,-33794,-76767,-46616,-11362,18650,40538,64293,46699,-44931,-61780,78887,96260,4262,-42091,94278,91384,21854,64726,-67858,-34249,-11931,30602,-24580,-20698,54433,-60711,-68206,65968,15001,63619,64387,94321,94220,54261,98887,40329,7704,19011,-35255,87414,57179,-95500,64681,-8117,81851,-83202,-44183,36651,-82557,7181,38357,-57647,62176,-15364,85221,22876,-12358,69436,6546,-64316,48926,-68450,-41625,-33727,96878,29827,51184,61598,-79841,84684,79517,-26177,-34520,12549,-93258,-46803,-70096,-57942,77999,-84330,-94149,-58410,92947,49512,-31085,-91546,37988,91099,9551,-11120,92699,-85917,86929,-49548,-48035,79493,21804,-96132,48651,-31431,-31350,-92476,-44179,33383,63969,-86148,-32926,-17775,46551,21175,35676,-15457,70484,-61240,86931,-87147,20190,-99590,-82914,-49881,79208,-37205,2552,46650,30961,-43897,45422,-12118,-59997,-61148,16296,-99049,66470,23923,-22199,40768,-55812,-21853,71964,-12366,80837,-55343,-75649,10538,17764,-63688,616,-63961,-63402,-93761,82930,43964,52197,-89595,54916,52162,9277,-94404,9105,82358,80385,-89520,-59296,-12140,-20614,92925,98055,-5153,82430,-66636,43145,64231,-89441,77846,-81694,-36432,4290,-78314,-5075,-3915,19554,-76849,57326,69271,-88496,-9246,-51991,58694,-64474,-42440,-73516,1976,19707,99864,-74358,-54214,94201,97084,34019,24586,-4130,-46138,-72222,32218,71357,-4729,46125,97648,-92771,46704,18379,69692,-62848,-8062,-18372,662,4195,-90910,-77901,-79395,-32994,97255,73096,-42530,-78691,49363,53905,-93371,70327,-52570,30446,15526,-63511,60015,58330,-85968,-9007,98654,-82718,-40703,95027,19820,-4289,-37308,41551,-43230,69516,67762,99206,48233,19560,71946,71895,68299,46701,48241,-52723,7328,-40548,33595,-95371,-51745,17942,-85209,8343,-18717,39819,-75289,-76404,-69992,38416,48420,-63108,-42174,-45124,80351]))

print(sol.maxTotalFruits([[2,8],[6,3],[8,6]],5, 4))
print(sol.maxTotalFruits([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]],5, 4))
print(sol.maxTotalFruits([[200000,10000]],200000,200000))