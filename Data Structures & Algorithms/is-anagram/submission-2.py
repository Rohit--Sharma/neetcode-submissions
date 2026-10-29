class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = {}
        t_hash = {}
        for ch in s:
            if ch in s_hash:
                s_hash[ch] += 1
            else:
                s_hash[ch] = 1
        for ch in t:
            if ch in t_hash:
                t_hash[ch] += 1
            else:
                t_hash[ch] = 1

        for ch in s_hash:
            if ch not in t_hash or t_hash[ch] != s_hash[ch]:
                return False
        for ch in t_hash:
            if ch not in s_hash or t_hash[ch] != s_hash[ch]:
                return False
        
        return True