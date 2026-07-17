class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        
        queue, visited, dist = deque(), set(), 0

        # multi source BFS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))


        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if (r < 0 or c < 0 
                    or r >= ROWS or c >= COLS 
                    or (r,c) in visited
                    or grid[r][c] == -1):
                    continue

                # vist, modify in place
                grid[r][c] = min(grid[r][c], dist)
                visited.add((r,c))

                # add neighbours to queue
                for dr, dc in dirs:
                    queue.append((r+dr, c+dc))

            # incr dist?
            dist += 1
        
