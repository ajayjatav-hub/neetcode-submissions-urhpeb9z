class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        mx = 0
        while r<len(prices):
            if prices[r]<=prices[l]:
                l =r
                r = l+1
            else:
                diff = prices[r]-prices[l]
                mx = max(diff,mx)
                r+=1
        return mx