class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s)-1

        while lp < rp:
            if not s[lp].isalnum():
                lp += 1
                continue
            if not s[rp].isalnum():
                rp -= 1
                continue
            if s[rp].lower() != s[lp].lower():
                return False

            rp -= 1
            lp += 1
        return True