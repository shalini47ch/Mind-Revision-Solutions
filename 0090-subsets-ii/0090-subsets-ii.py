class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #here we need to handle duplicates as well
        nums.sort()
        n=len(nums)
        res=[]
        self.helper(0,[],res,nums,n)
        return res

    def helper(self,ind,ds,res,nums,n):
        res.append(ds.copy())
        for i in range(ind,n):
            if(i>ind and nums[i]==nums[i-1]):
                continue
            ds.append(nums[i])
            self.helper(i+1,ds,res,nums,n)
            ds.pop()
        