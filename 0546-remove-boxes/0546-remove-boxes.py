class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        #we get k*k points 
        n=len(boxes)
        #now applying memo to solve this 
        dp={}
        def helper(l,r,k):
            if(l>r):
                return 0
            if(l,r,k) in dp:
                return dp[(l,r,k)]
            #remove boxes along with k
            ans=(k+1)**2+helper(l+1,r,0)
            #now the next step is to remove from the middle and then merge them together and the loop will iterate from l+1,r+1
            for m in range(l+1,r+1):
                if(boxes[m]==boxes[l]):
                    #lets do for middle and then merged
                    middle=helper(l+1,m-1,0)
                    #now similarly do for merged
                    merged=helper(m,r,k+1)
                    ans=max(ans,middle+merged)
            dp[(l,r,k)]=ans
            return dp[(l,r,k)]
        return helper(0,n-1,0)
        

        