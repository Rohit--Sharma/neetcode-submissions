class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1s = 0
        i = 0
        while i < len(nums):
            curr = 0
            while i < len(nums) and nums[i] == 1:
                curr += 1
                i += 1
            max1s = max(max1s, curr)
            i += 1
        return max1s