class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prods = [1] * len(nums)
        prefix_prods[0] = nums[0]
        suffix_prods = [1] * len(nums)
        suffix_prods[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix_prods[i] = nums[i] * prefix_prods[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_prods[i] = nums[i] * suffix_prods[i + 1]
        
        # print(prefix_prods)
        # print(suffix_prods)

        res = []
        for i in range(len(nums)):
            r = 1
            if i - 1 >= 0:
                r *= prefix_prods[i - 1]
            if i + 1 <= len(nums) - 1:
                r *= suffix_prods[i + 1]
            res.append(r)
        return res
