class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxi=0 #this will help us to find the maximum profit
        for i in range(1,len(prices)):
            mini=min(mini,prices[i])
            currprice=prices[i]-mini
            maxi=max(maxi,currprice)
        return maxi


        