class Solution:
    #create a helper function to find a palindrome
    def isPalindrome(self,i,j,s,n,dp):
        if(i>=j):
            return True 
        if(dp[i][j]!=-1):
            return dp[i][j]
        if(s[i]==s[j]):
            dp[i][j]=self.isPalindrome(i+1,j-1,s,n,dp)
            return dp[i][j]
        dp[i][j]=False
        return dp[i][j]
    
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxi=-sys.maxsize
        start=0
        dp=[[-1 for i in range(n+1)]for j in range(n+1)]
        #iterate through the given string
        for i in range(0,n):
            for j in range(i,n):
                if(self.isPalindrome(i,j,s,n,dp)):
                    if(j-i+1>maxi):
                        maxi=j-i+1
                        start=i
        return s[start:start+maxi]

        