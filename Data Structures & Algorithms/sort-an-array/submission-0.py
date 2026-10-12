class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left, right = nums[:mid], nums[mid:]

            left = mergeSort(left)
            right = mergeSort(right)

            return merge(left, right)

        def merge(left, right):
            res = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            while l < len(left):
                res.append(left[l])
                l += 1
            while r < len(right):
                res.append(right[r])
                r += 1
            return res

        return mergeSort(nums)