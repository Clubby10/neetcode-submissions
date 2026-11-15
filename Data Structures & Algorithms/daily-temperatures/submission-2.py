class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # tmp, idx

        for idx, tmp in enumerate(temperatures):
            while stack and stack[-1][0] < tmp:
                stackTmp, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append((tmp, idx))

        return res