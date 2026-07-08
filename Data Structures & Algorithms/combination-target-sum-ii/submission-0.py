class Solution:
    '''
    backtracking 
    - at each point:
        - choose idx i 
            - continue path with idx i chosen
        - don't choose idx i (backtrack)
            - continue path with idx i not chosen
    '''

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        candidates.sort()



        def dfs(i, comb, total):
            if total == target:
                ans.append(comb.copy())
                return
            if total > target or i >= n:
                return


            # choose idx i 
            candidate = candidates[i]
            comb.append(candidate)
            dfs(i+1, comb, total+candidate) # continue path with i chosen
            
            # don't choose idx i 
            comb.pop()
            j = 1
            while i+j < n and candidates[i+j] == candidate:
                j += 1
            dfs(i+j, comb, total)


        dfs(0, [], 0)
        return ans