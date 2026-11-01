class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_len = 0

        num_set = set(nums)

        for n in nums:
            if n - 1 in num_set:
                # If n - 1 is already in the set, then it can't start a sequence
                continue
            
            curr_len = 1
            nxt = n + 1
            # Start a new sequence
            while nxt in num_set:
                curr_len += 1
                nxt += 1
            
            if curr_len > longest_len:
                longest_len = curr_len

        return longest_len
