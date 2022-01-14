from typing import List
import collections
import math
import sys
import os
from common import create2DArray, __location__
import json

def numPermsDISequence(s: str) -> int:
    ans = [0]

    def helper(cur_idx, prev_selected_n, c_bank, selected_arr):
        if not c_bank and cur_idx >= len(s) - 1: 
            ans[0] += 1
            print(selected_arr)
            return
        
        c = s[cur_idx]
        for i in c_bank:
            new_set = set(c_bank)
            selected = i
            new_set.remove(i)
            if prev_selected_n is not None and c == 'D' and prev_selected_n > i:
                helper(cur_idx+1, selected, new_set, selected_arr + [selected])
            elif prev_selected_n is not None and c == 'I' and prev_selected_n < i:
                helper(cur_idx+1, selected, new_set, selected_arr + [selected])
            elif prev_selected_n is None:
                helper(cur_idx, selected, new_set, selected_arr + [selected])
            #new_set.add(i)

    cur_set = set([i for i in range(len(s) + 1)])
    helper(0, None, cur_set, [])
    return ans[0]

#print(numPermsDISequence('DID'))
print(numPermsDISequence('IDDDIIDIIIIIIIIDIDID'))