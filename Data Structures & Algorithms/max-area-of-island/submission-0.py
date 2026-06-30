class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        maxarea = 0

        def dfs(i, j, curr_area):
            if i < 0 or i >= ROWS:
                return curr_area
            if j < 0 or j >= COLS:
                return curr_area
            if grid[i][j] == 0:
                return curr_area
            
            grid[i][j] = 0  # visit curr
            curr_area += 1  # 

            for d in directions:
                curr_area += dfs(i + d[0], j + d[1], 0)
            return curr_area
                

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    island_area = dfs(i, j, 0)

                    maxarea = max(maxarea, island_area)


        return maxarea
        