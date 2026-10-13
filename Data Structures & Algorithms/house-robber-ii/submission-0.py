class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(houses):
            dp = {}

            def dfs(i):
                if i >= len(houses):
                    return 0

                if i in dp:
                    return dp[i]

                rob = houses[i] + dfs(i + 2)
                skip = dfs(i + 1)

                dp[i] = max(rob, skip)
                return dp[i]

            return dfs(0)


        return max(helper(nums[:-1]), helper(nums[1:]))