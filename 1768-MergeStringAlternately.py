from typing import List
import collections
import itertools
import math
from common import TreeNode, convertToTree

def mergeAlternately(w1, w2):
    return "".join([a + b for a,b in itertools.zip_longest(w1, w2, fillvalue='')])
print(mergeAlternately("1111", "222222"))
print([[a,b] for a,b in itertools.zip_longest("1111", "22222", fillvalue='')])