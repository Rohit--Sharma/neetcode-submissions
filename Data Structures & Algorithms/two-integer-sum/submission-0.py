class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for i in range(len(nums)):
            if target - nums[i] in idxs:
                return [idxs[target - nums[i]], i]
            idxs[nums[i]] = i
        return None
