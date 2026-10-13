class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {} # (r, c) : ways
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            if (r, c) in dp:
                return dp[(r, c)]

            right = dfs(r, c + 1)
            down = dfs(r + 1, c)

            dp[(r, c)] = right + down

            return dp[(r, c)]

        return dfs(0, 0)

            