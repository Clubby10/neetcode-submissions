class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {} # val : freq
        n = len(nums)

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        res = []
        for val in freq:
            if freq[val] > n / 3:
                res.append(val)

        return res
