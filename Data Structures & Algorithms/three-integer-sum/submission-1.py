class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(1) space (excluding sorting) solution based on 2 sum for sorted arrays
        # O(n^2) time complexity
        
        nums.sort()
        nums_len = len(nums)
        res = set()
        for i in range(nums_len):
            target = -nums[i]

            j = i + 1
            k = nums_len - 1
            
            while j < k:
                if nums[j] + nums[k] == target:
                    res.add((nums[i], nums[j], nums[k]))
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        
        return list(res)
