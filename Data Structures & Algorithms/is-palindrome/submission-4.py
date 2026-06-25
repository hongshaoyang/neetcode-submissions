class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed = []
        for l in s:
            if l.isalnum():
                trimmed.append(l.lower())

        i, j = 0, len(trimmed) - 1
        while i < j:
            if trimmed[i] != trimmed[j]:
                return False
            i += 1
            j -= 1

        return True

        