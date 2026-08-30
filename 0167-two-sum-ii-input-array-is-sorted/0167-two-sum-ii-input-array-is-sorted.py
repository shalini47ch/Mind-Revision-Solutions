class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        n=len(nums)
        left=0
        right=n-1
        while(left<right):
            if(nums[left]+nums[right]<target):
                left+=1
            elif(nums[left]+nums[right]>target):
                right-=1
            else:
                #as it is 1 indexed so here we add one
                res.extend([left+1,right+1])
                left+=1
                right-=1
        return res
       