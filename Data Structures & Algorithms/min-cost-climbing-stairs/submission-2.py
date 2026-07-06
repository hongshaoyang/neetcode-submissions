class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        start
            - start at 0
                - pay 0, jump 1
                - pay 0, jump 2
            - start at 1
                - pay 1, jump 1
                - pay 1, jump 2
        '''

        cache = {}

        def dfs(i):
            '''
            dfs(i) = min cost to reach top, starting from step i

            base case - i == n or i > n
            '''
            if i >= len(cost):
                return 0


            if i in cache:
                return cache[i]

            # pay cost i
            curr = cost[i]

            # add minimum

            if i+1 in cache:
                one_step = cache[i+1]
            else:
                one_step = dfs(i+1)
                cache[i+1] = one_step

            if i+2 in cache:
                two_step = cache[i+2]
            else:
                two_step = dfs(i+2)
                cache[i+2] = two_step



            delta = min(dfs(i+1), dfs(i+2))
            return curr + delta


        return min(dfs(0), dfs(1))


            
        