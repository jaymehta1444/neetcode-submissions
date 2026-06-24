class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        new = ''
        for l in s:
            if l.isalnum():
                new += l
        return new == new[::-1]