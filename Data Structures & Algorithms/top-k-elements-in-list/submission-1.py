import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ex: nums: [1, 2, 2, 3, 3, 3]

        # Store frequencies: freq = {1:1, 2:2, 3:3}
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Store the frequencies as tuples in max heap by frequencies
        max_heap = []
        for n, f in freq.items():
            heapq.heappush(max_heap, (-f, n))
        
        return [heapq.heappop(max_heap)[1] for _ in range(k)]
