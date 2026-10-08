class Solution:
    def maxArea(self, heights: List[int]) -> int:

        mx = 0
        rp = len(heights)-1
        lp = 0

        while lp < rp:
            area = (rp - lp) * min(heights[rp], heights[lp])
            mx = max(mx, area)

            if heights[rp] < heights[lp]:
                rp -= 1
            else:
                lp += 1
        

        return mx