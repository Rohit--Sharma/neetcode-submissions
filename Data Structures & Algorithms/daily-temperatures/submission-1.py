class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # DP approach (only O(1) extra space compared to O(n) needed for the stack approach)

        l = len(temperatures)
        res = [0] * l
        i = l - 1
        while i >= 0:
            j = i + 1
            while j < l and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    break
                j += res[j]
            if j < l and temperatures[j] > temperatures[i]:
                res[i] = j - i
                
            i -= 1

        return res