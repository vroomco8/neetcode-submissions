class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        stn = set(nums)

        for n in stn:
            if (n-1) not in stn:
                cur = 1
                while (n + cur) in stn:
                    cur += 1
                res = max(cur, res)
        return res
        