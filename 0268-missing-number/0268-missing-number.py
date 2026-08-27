class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #use cyclic sort to solve this 
        n=len(nums)
        i=0
        #since it is from 0 till n so correct is nums[i] else it will be nums[i]-1
        while(i<n):
            correct=nums[i]
            if(nums[i]<n and nums[i]!=nums[correct]):
                #perform the swap
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        for i in range(0,n):
            if(nums[i]!=i):
                return i
        return n
       