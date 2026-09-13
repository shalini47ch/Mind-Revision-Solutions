class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        dp={}
        return self.helper(0,len(cuts)-1,cuts,dp)
    
    #now here we will write the recursive code 
    def helper(self,i,j,cuts,dp):
        if(i+1==j):
            return 0
        if(i,j) in dp:
            return dp[(i,j)]
        mini=sys.maxsize
        #now here we perform the split
        for k in range(i+1,j):
            #so here we will find the cost
            cost=(cuts[j]-cuts[i])+self.helper(i,k,cuts,dp)+self.helper(k,j,cuts,dp)
            mini=min(mini,cost)
        dp[(i,j)]=mini
        return dp[(i,j)]

        