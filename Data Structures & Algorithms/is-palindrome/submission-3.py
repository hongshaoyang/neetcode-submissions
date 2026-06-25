class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            a = s[i]
            b = s[j] 
            if not a.isalnum():
                i += 1
                continue
            if not b.isalnum():
                j -= 1
                continue
            if a.lower() != b.lower():
                return False
            i += 1
            j -= 1
        return True

        