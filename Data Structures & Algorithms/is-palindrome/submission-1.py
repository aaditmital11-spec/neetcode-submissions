class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1
        g = s.lower()
        while l < r:
            if not g[l].isalnum():
                l += 1
                continue
            if not g[r].isalnum():
                r -= 1
                continue
            if g[l] != g[r]:
                return False
            l += 1
            r -= 1
        return True