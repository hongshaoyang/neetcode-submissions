from collections import Counter

class Solution:
    '''
    sol 2 - track curr index in nums. 2 ways forward:
        - visit current, add curr index to sum
        - skip current, move to next 
    '''
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        def dfs(idx, total, comb):
            '''
            idx = curr idx
            total = sum of current combination
            comb = current combination
            '''
            # base case 1  - target reached
            if total == target:
                ans.append(comb.copy())
                return 

            for new_i in range(idx, len(nums)):
                candidate = nums[new_i]
                new_total = total + candidate
                if new_total > target:
                    return
                comb.append(candidate)
                dfs(new_i, new_total, comb)
                comb.pop()

        dfs(0, 0, [])
        return ans