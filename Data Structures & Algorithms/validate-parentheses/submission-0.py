from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        m = {"}": "{", "]": "[", ")": "("}
        for char in s:
            if char in ["(", "{", "["]:
                d.append(char)
            else:
                if len(d) == 0:
                    return False
                _open = d.pop()
                if m[char] != _open:
                    return False 
        return len(d) == 0
        