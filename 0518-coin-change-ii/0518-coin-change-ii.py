class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #return the no of combinations that make the amount 
        n=len(coins)
        dp=[[-1 for i in range(amount+1)]for j in range(n+1)]
        return self.helper(n-1,coins,amount,n,dp)

    def helper(self,ind,coins,amount,n,dp):
        #we will move from n-1 to 0
        if(ind==0):
            if(amount%coins[ind]==0):
                return 1
            else:
                return 0
        if(dp[ind][amount]!=-1):
            return dp[ind][amount]
        #now there are two options notpick and pick
        notpick=self.helper(ind-1,coins,amount,n,dp)
        pick=0
        if(coins[ind]<=amount):
            pick=self.helper(ind,coins,amount-coins[ind],n,dp)
        dp[ind][amount]=(pick+notpick)
        return dp[ind][amount]
        