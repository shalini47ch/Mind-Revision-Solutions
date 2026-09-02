class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #here we need to return the area of the largest rectangle so lets use the concept of nsl and nsr
        maxarea=0
        left=self.nsl(heights)
        right=self.nsr(heights)
        for i in range(0,len(heights)):
            #area is basically width*height
            area=(right[i]-left[i]-1)*heights[i]
            maxarea=max(maxarea,area)
        return maxarea
    def nsl(self,heights):
        #use concept of stacks to solve this 
        n=len(heights)
        stack=[]
        ans=[]
        for i in range(0,n):
            while(stack and heights[stack[-1]]>=heights[i]):
                stack.pop()
            if(len(stack)==0):
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(i)
        return ans
    
    #now create a helper function to find nsr
    def nsr(self,heights):
        n=len(heights)
        stack=[]
        ans=[]
        for i in range(n-1,-1,-1):
            while(stack and heights[stack[-1]]>=heights[i]):
                stack.pop()
            if(len(stack)==0):
                ans.append(n)
            else:
                ans.append(stack[-1])
            stack.append(i)
        return ans[::-1]
       