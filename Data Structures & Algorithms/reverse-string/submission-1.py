class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        i = 0
        while i < l//2:
            t = s[l - i - 1]
            s[l - i - 1] = s[i]
            s[i] = t
            i += 1