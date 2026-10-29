class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            s_ = str(sorted(s))
            if s_ in anagrams:
                anagrams[s_].append(s)
            else:
                anagrams[s_] = [s]
        
        return [vals for vals in anagrams.values()]