class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(i, j):
            # boundary checks
            if i < 0 or i >= ROWS:
                return
            if j < 0 or j >= COLS:
                return

            # valid dfs check
            if grid[i][j] == "0":
                return

                
            grid[i][j] = "0" # visit curr and set to "0" lol

            for d in directions:
                dfs(i + d[0], j + d[1])
        

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands