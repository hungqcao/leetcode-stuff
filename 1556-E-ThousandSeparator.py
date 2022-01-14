from typing import Counter, List
import collections
import math
import sys
from common import create2DArray

def thousandSeparator(n: int) -> str:
    val = str(n)
    size = len(val)
    chunks = [val[i-3:i] if i >=3 else val[0:i] for i in range(len(val), 0, -3)]
    return '.'.join(reversed(chunks))

print(thousandSeparator(1234412312123))

print([1,2,3][::-1])