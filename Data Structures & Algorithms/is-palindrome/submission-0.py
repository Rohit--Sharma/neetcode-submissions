class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = ''
        for ch in s:
            if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch >= '0' and ch <= '9'):
                sanitized += ch.lower()
        return sanitized == sanitized[::-1]