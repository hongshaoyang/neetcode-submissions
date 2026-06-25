from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(s)
        counter2 = Counter(t)
        for e, cnt in counter1.items():
            if not (e in counter2 and cnt == counter2[e]):
                return False
        for e, cnt in counter2.items():
            if not (e in counter1 and cnt == counter1[e]):
                return False
        return True




