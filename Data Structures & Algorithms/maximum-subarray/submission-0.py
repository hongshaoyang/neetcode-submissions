class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def dfs(i, started):
            '''
            what is the max subarray sum we can get starting from 
            idx i, given whether we are already inside a subarray (flag)? 
            i: current idx of array
            started: has a subarray already started?
            '''
            
            # base case
            if i == len(nums):
                return 0 if started else float("-inf")

            if started:
                # we have started and are inside a subarray
                return max(
                    0,                       # stop the subarray here
                    nums[i] + dfs(i+1, True) # continue subarray
                )
            else:
                # we have not started yet 
                return max(
                    dfs(i+1, False),         # skip curr, stay outside
                    nums[i] + dfs(i+1, True) # start a new subarray at i
                )

        return dfs(0, False)