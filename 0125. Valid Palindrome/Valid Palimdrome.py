class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for i in s:
            if i.isalnum():
                new += i
        if new == new[::-1]:
            return True
        else:
            return False