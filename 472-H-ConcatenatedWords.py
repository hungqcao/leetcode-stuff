from typing import List
import collections

def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    d = set(words)
    memo = {}
    def dfs(word):
        if word in memo: return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if prefix in d and suffix in d:
                return True
            elif prefix in d and dfs(suffix):
                return True
            elif suffix in d and dfs(prefix):
                return True
        return False
    res = []
    for w in words:
        if dfs(w):
            memo[w] = True
            res.append(w)
        else:
            memo[w] = False

    return res

#print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))