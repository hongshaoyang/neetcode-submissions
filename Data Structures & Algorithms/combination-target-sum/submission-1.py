from collections import Counter

class Solution:
    '''
    sol 2 - track curr index in nums. 2 ways forward:
        - visit current, add curr index to sum
        - skip current, move to next 
    '''
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(idx, total, comb):
            '''
            idx = curr idx
            total = sum of current combination
            comb = current combination
            '''
            # base case 1 
            if total == target:
                ans.append(comb.copy())
                return 

            # base case 2
            if total > target or idx >= len(nums):
                return


            # choose to include nums[i]
            comb.append(nums[idx])
            # stay at same idx
            dfs(idx, total+nums[idx], comb)
            # backtrack
            comb.pop()

            # skip nums[i]
            dfs(idx+1, total, comb)


        dfs(0, 0, [])
        return ans