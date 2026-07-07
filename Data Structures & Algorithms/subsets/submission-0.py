class Solution:
    '''
    at idx i:
        - 
        - choose i, move to next idx
        - don't choose i, move to next idx



    
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []



        def dfs(idx, subset):
            # ending condition
            if idx >= len(nums):
                ans.append(subset.copy())
                return

            

            subset.append(nums[idx])
            dfs(idx+1, subset)



            subset.pop()
            dfs(idx+1, subset)


            return


        dfs(0, [])

        return ans
        