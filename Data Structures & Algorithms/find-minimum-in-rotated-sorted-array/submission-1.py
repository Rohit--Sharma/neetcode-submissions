class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # print(l, r, mid)
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]

            if nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                return nums[l]
            elif nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]