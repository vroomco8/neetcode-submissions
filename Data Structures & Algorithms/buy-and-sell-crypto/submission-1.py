class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curSell = 0
        curProfit = 0
        mxProfit = 0
        n = len(prices)

        for i in range(n-1, -1, -1):
            if curSell < prices[i]:
                curSell = prices[i]
            else:
                curProfit = curSell - prices[i]
                mxProfit = max(mxProfit, curProfit)
        
        return mxProfit
