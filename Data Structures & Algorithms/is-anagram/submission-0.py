class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        chs = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            chs[s[i]] = chs.get(s[i], 0) + 1
            chs[t[i]] = chs.get(t[i], 0) - 1

        return not any(chs.values()) 

        