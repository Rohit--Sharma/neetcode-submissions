class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute-force:
        # Convert to 2Sum problem, for each number, find two numbers that make the number add to 0
        seen = {}
        res = []
        res_set = set()
        for i, n in enumerate(nums):
            seen[n] = i
        
        for i, n in enumerate(nums):
            target = -n

            for j, m in enumerate(nums):
                if j <= i:
                    continue
                if target - m in seen and seen[target - m] != i and seen[target - m] != j:
                    res_set.add(tuple(sorted([n, m, target - m])))
                    # res.append([n, m, target - m])
        
        return list(res_set)