class Solution:
    def trap(self, height: List[int]) -> int:
        #here lets create two helper functions ngr and ngl
        n=len(height)
        left=self.ngl(height)
        right=self.ngr(height)
        su=0
        #traverse through height and find the sums
        for i in range(0,n):
            area=min(left[i],right[i])-height[i]
            su+=area
        return su

    def ngl(self,height):
        n=len(height)
        left=[0 for i in range(n)]
        left[0]=height[0]
        #now filling the other part
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        return left
    
    #now create a helper to find ngr
    def ngr(self,height):
        n=len(height)
        right=[0 for i in range(n)]
        right[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        return right
    


       