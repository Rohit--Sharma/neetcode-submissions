class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ex: nums: [1, 2, 2, 3, 3, 3]

        # Store frequencies: freq = {1:1, 2:2, 3:3}
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Bucket the numbers based on frequency
        freq_to_nums = [[] for _ in range(len(nums) + 1)]
        for n, f in freq.items():
            freq_to_nums[f].append(n)
        
        # Keep adding numbers to the result from buckets in descending order of frequencies
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq_to_nums[i]:
                res.append(n)
                if len(res) == k:
                    return res