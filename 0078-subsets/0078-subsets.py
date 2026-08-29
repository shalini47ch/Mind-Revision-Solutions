class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #use backtracking to solve this 
        res=[]
        n=len(nums)
        self.helper(0,[],res,nums,n)
        return res

    def helper(self,ind,ds,res,nums,n):
        res.append(ds.copy())
        for i in range(ind,n):
            ds.append(nums[i])
            self.helper(i+1,ds,res,nums,n)
            ds.pop()
        






        