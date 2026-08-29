class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        used=[False for i in range(n)]
        self.helper(nums,[],res,used,n)
        return res

    def helper(self,nums,ds,res,used,n):
        if(len(ds)==n):
            res.append(ds.copy())
            return 
        for i in range(0,n):
            if(used[i]):
                continue
            used[i]=True
            ds.append(nums[i])
            self.helper(nums,ds,res,used,n)
            used[i]=False
            ds.pop()
            

       