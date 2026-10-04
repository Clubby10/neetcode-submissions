class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, total = float("infinity"), 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if res == float("infinity") else res

