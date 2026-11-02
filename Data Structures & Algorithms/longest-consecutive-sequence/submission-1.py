class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # One pass solution using interval-merging hash maps solution.
        # Hard to follow, review again!

        # Stores the length of consecutive sequence this number is part of.
        # The number is only updated for boundaries of sequences, internal sequence numbers may have older length which need not be updated
        # due to the way the algorithm works. (we only check boundaries to merge sequences)
        boundaries_map = {}
        max_len = 0
        for n in nums:
            if n in boundaries_map:
                continue
            
            # Gets length of left and right adjacent sequences (0 if they don't exist)
            left = boundaries_map.get(n - 1, 0)
            right = boundaries_map.get(n + 1, 0)

            # Merge sequences including n
            total_len = left + right + 1
            max_len = max(max_len, total_len)

            # Mark n as visited
            boundaries_map[n] = total_len

            # Update left and right boundaries of the current consecutive sequence.
            # This ensures that future lookups at the far ends of the sequence get the correct length
            # (Again note that we are not updating every value in the sequence as its never looked up in the future.)
            boundaries_map[n - left] = total_len
            boundaries_map[n + right] = total_len

        return max_len