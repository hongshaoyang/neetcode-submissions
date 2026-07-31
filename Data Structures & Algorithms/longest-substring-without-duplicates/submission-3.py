class Solution:
    '''
    hashset backed by set instead of dict (dict also works)
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashset = set()
        lo, hi = 0, 0
        maxlen = 0 

        while True:
            if hi >= len(s):
                break


            c = s[hi]
            if c in hashset: 
                hashset.remove(s[lo])

                lo += 1
            else:
                hashset.add(c)
                maxlen = max(maxlen, hi-lo+1)

                hi += 1
        return maxlen