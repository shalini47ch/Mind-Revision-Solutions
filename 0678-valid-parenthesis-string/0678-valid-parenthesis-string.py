class Solution:
    def checkValidString(self, s: str) -> bool:
        #use recursion+memo to solve this 
        n=len(s)
        dp=[[-1 for i in range(n+1)]for j in range(n+1)]
        return self.helper(0,0,s,n,dp)

    def helper(self,ind,count,s,n,dp):
        if(count<0):
            return False
        if(ind==n):
            return count==0
        if(dp[ind][count]!=-1):
            return dp[ind][count]
        #now there are cases of opening bracket closing bracket or either of them 
        ch=s[ind]
        if(ch=="("):
            dp[ind][count]=self.helper(ind+1,count+1,s,n,dp)
            return dp[ind][count]
        elif(ch==")"):
            dp[ind][count]=self.helper(ind+1,count-1,s,n,dp)
            return dp[ind][count]
        else:
            #this is the case of *
            dp[ind][count]=(self.helper(ind+1,count+1,s,n,dp)
            or self.helper(ind+1,count-1,s,n,dp) or 
            self.helper(ind+1,count,s,n,dp))
            return dp[ind][count]


        