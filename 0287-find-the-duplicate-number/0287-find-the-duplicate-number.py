from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #use the concept of cyclic sort to solve this 
        n=len(nums)
        i=0
        while(i<n):
            correct=nums[i]-1
            if(nums[i]!=nums[correct]):
                #perform the swap
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        for i in range(0,n):
            if(nums[i]!=i+1):
                return nums[i]
       

       