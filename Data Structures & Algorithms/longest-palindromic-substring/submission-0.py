class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        res_idx = 0 # starting idx of best palindrome
        res_len = 0 # len of best palindrome

        for i in range(len(s)):

            # step 2 - odd len
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:


                if (r-l + 1) > res_len:
                    res_len = r-l + 1
                    res_idx = l

                # update
                l -= 1
                r += 1

            # step 2 - even len
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:

                if (r-l + 1) > res_len:
                    res_len = r-l + 1
                    res_idx = l
                
                # update
                l -= 1
                r += 1

        return s[res_idx : res_idx + res_len]

        
        