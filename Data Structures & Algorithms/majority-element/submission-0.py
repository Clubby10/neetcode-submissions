class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {} # val : freq

        for num in nums:
            mp[num] = 1 + mp.get(num, 0)

        maxCount, res = 0, 0
        for m in mp:
            if mp[m] > maxCount:
                maxCount = mp[m]
                res = m
        return res
        