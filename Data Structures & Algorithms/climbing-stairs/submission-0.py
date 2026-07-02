class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        - change to bottom-up (N to 0)
        - to reach step i, you can only come from
            - step i-1 (1 step)
            - step i-2 (2 step)

        - dp works by classifying paths according to FINAL MOVE
            - every path to i ends with either
                - ... -> i-1 -> i      or
                - ... -> i-2 -> i
        '''

        if n <= 3:
            return n
        
        dp = [None for i in range(n+1)]
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
