class Solution:
    def __init__(self):
        self.sep = '#'

    def encode(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ''
        
        res = ''
        for s in strs:
            l = str(len(s))
            res += l + self.sep + s

        # print('Encoded:', res)
        return res

    def decode(self, s: str) -> List[str]:
        if not s or s == '':
            return []
        
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != self.sep:
                j += 1
            l = int(s[i : j])
            i = j + 1
            j = i + l
            res.append(s[i : j])
            i = j

        # print('Decoded:', res)
        return res
