class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = strs.sort()
        first = strs[0]
        last = strs[-1]

        ml = min(len(first), len(last))
        i = 0
        while i < ml and first[i] == last[i]:
            i += 1
        
        return first[:i]