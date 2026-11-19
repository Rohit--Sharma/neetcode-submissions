class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        l = len(temperatures)
        res = [0] * l

        i = 0
        while i < l:
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
            i += 1

        return res
