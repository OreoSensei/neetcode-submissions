class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        sorted_strs = strs.sort(key = sorted)
        ret = []
        i = 0

        while i < len(strs):
            temp = [strs[i]]
            i += 1

            while i < len(strs) and sorted(strs[i]) == sorted(temp[0]):
                temp.append(strs[i])
                i += 1
            ret.append(temp)
        return ret