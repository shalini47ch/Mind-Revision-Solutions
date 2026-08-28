class Solution:
    def maxArea(self, height: List[int]) -> int:
        #use two pointers to solve this 
        n=len(height)
        left=0
        right=n-1
        maxarea=0
        while(left<right):
            area=(right-left)*min(height[left],height[right])
            maxarea=max(maxarea,area)
            if(height[left]<height[right]):
                left+=1
            elif(height[right]<height[left]):
                right-=1
            else:
                left+=1
        return maxarea
        