class Solution:
    def rob(self, nums: List[int]) -> int:
        # top down
        dp = {}
        
        def dfs(i):
            if i >= len(nums):
                return 0

            if i in dp:
                return dp[i]

            # op 1: rob
            rob = nums[i] + dfs(i + 2)
            # op 2: skip
            skip = dfs(i + 1)

            dp[i] = max(rob, skip)

            return dp[i]

        return dfs(0)
