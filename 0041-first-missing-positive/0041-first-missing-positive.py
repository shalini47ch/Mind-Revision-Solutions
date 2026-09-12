class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #here we will use the concept of cyclic sort to solve this 
        i=0
        n=len(nums)
        while(i<n):
            correct=nums[i]-1
            if(1<=nums[i]<=n and nums[i]!=nums[correct]):
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        for i in range(0,n):
            if(nums[i]!=i+1):
                return i+1
        return n+1
        