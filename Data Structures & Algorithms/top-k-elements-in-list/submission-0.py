class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ex: nums: [1, 2, 2, 3, 3, 3]

        # Store frequencies: freq = {1:1, 2:2, 3:3}
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Convert dict to tuple: freq_tup = [(1, 1), (2, 2), (3, 3)]
        freq_tup = [(n, f) for n, f in freq.items()]

        # Sort the frequencies tuple in reverse order by frequencies
        # freq_tup = [(3, 3), (2, 2), (1, 1)]
        freq_tup.sort(key=lambda t: t[1], reverse=True)

        # Return top k frequency nums
        return [t[0] for t in freq_tup[:k]]
