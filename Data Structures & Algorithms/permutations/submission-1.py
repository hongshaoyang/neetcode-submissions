class Solution:
    '''
    3. backtracking
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        chosen = [False] * len(nums) 

        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                # skip chosen
                if chosen[i]:
                    continue

                # choose nums[i]
                perm.append(nums[i])
                chosen[i] = True

                # recurse
                dfs(perm)

                # backtrack: un-choose nums[i]
                perm.pop()
                chosen[i] = False


        dfs([])
        return res

        