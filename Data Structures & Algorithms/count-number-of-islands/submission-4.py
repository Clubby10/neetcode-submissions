class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(row, col):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0"):
                return 0

            grid[row][col] = "0"

            for dr, dc in dirs:
                dfs(row + dr, col + dc)

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands