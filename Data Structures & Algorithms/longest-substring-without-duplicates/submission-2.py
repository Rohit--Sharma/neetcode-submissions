class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        l = len(s)
        if l == 1:
            return 1

        i = 0
        j = 1
        seen = set()
        seen.add(s[i])
        longest = 1
        while i < l and j < l:
            while j < l and s[j] not in seen:
                seen.add(s[j])
                longest = max(longest, j - i + 1)
                j += 1

            # print(i, j, seen)
            while i < l and j < l and s[i] != s[j]:
                # print(i, seen)
                seen.remove(s[i])
                i += 1
            
            i += 1
            j += 1

        return longest

