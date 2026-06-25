class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        end = 0 
        max_len = 0 
        d = dict()
        while True:
            # break if needed 
            if end >= len(s):
                return max_len

            c = s[end]
            if c not in d:
                d[c] = True
                max_len = max(max_len, (end - start + 1))
                end += 1
            else:
                start_char = s[start]
                del d[start_char]
                start += 1
            