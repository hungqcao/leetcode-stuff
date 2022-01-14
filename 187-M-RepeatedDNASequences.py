from typing import List
import collections

def findRepeatedDnaSequences(s: str) -> List[str]:
    seq_len = 10
    mask = (1 << (seq_len*2)) - 1
    map = {'A':0, 'C':1,'G':2,'T':3}
    res,seen = set(), set()
    sequence = 0
    for i in range(seq_len):
        sequence <<= 2
        sequence &= mask
        sequence |= map[s[i]]
    print("{0:b}".format(sequence))
    seen.add(sequence)
    for i in range(seq_len, len(s)):
        sequence <<= 2
        sequence &= mask
        sequence |= map[s[i]]
        if sequence in seen:
            res.add(s[i-seq_len+1:i+1])
        else:
            seen.add(sequence)
    return res


print(findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))