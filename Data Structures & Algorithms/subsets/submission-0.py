class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i: int, subset: list[int]) -> None:
            nonlocal res
            res.append(subset.copy())

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()


        backtrack(0, [])
        return res