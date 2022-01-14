from typing import List
import collections
import math

def deckRevealedIncreasing(deck: List[int]) -> List[int]: 
    deck, size = sorted(deck), len(deck)
    ans = [0 for i in range(size)]
    index = [i for i in range(size)]
    for card in deck:
        ans[index.pop(0)] = card
        if index:
            index.append(index.pop(0))
    return ans

print(deckRevealedIncreasing([17,13,11,2,3,5,7]))