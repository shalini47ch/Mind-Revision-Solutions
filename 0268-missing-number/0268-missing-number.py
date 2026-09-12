class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #here we need to return the missing number
        #lets use cyclic sort to solve this 
        i=0
        n=len(nums)
        while(i<n):
            correct=nums[i]
            if(nums[i]<n and nums[i]!=nums[correct]):
                #perform swap
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        for i in range(0,n):
            if(nums[i]!=i):
                return i
        return n
       