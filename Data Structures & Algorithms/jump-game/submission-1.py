class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False

            maxReach = max(maxReach, i + nums[i])

        return True if maxReach >= len(nums) - 1 else False