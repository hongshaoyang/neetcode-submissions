class Solution:
    '''
    - simpler solution: BFS for every INF cell 
    '''
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        
        def bfs(r,c):
            queue, visited, dist = deque(), set(), 0

            queue.append((r,c))

            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    if (r < 0 or c < 0
                        or r >= ROWS or c >= COLS
                        or (r,c) in visited
                        or grid[r][c] == -1):
                        continue

                    if grid[r][c] == 0:
                        return dist

                    visited.add((r,c))

                    # add neighbours to queue
                    for dr, dc in dirs:
                        queue.append((r+dr, c+dc))

                dist += 1

            return INF
        
        # bfs 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)

