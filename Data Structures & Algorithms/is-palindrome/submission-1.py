class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(s.split(" ")).lower()
        
        lp = 0
        rp = len(s)-1

        while lp < rp:
            if not s[lp].isalnum():
                lp += 1
            if not s[rp].isalnum():
                rp -= 1
            else:
                if s[rp] != s[lp]:
                    return False
                rp -= 1
                lp += 1
        return True