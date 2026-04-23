class Solution:
    def isPalindrome(self, s: str) -> bool:
        ts = "".join(char for char in s if char.isalnum())
        ts = ts.lower()
        l = len(ts)
        i, j = 0, l - 1
        while i < l//2:
            if ts[i] != ts[j]:
                return False
            i += 1
            j -= 1
        return True