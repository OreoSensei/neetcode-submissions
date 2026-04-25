class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        m = min(l1, l2)
        ret = ""
        for i in range(m):
            ret += word1[i] + word2[i]
        if l1 < l2:
            ret += word2[i+1:]
        else:
            ret += word1[i+1:]
        return ret