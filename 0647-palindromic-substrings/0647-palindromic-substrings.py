class Solution:
    def countSubstrings(self, s: str) -> int:
        #first create a helper function to check for the logic of palindrome
        n=len(s)
        count=0
        dp=[[-1 for i in range(n+1)]for j in range(n+1)]
        for i in range(0,n):
            for j in range(i,n):
                if(self.isPalindrome(i,j,s,dp)):
                    count+=1
        return count
                    
    def isPalindrome(self,i,j,s,dp):
        if(i>=j):
            return True
        if(dp[i][j]!=-1):
            return dp[i][j]
        if(s[i]==s[j]):
            dp[i][j]=self.isPalindrome(i+1,j-1,s,dp)
            return dp[i][j]
        else:
            dp[i][j]=False
            return dp[i][j]






    


       