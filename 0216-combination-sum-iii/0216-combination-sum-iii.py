class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        #here we need numbers that sum upto k
        res=[]
        self.helper(1,[],res,target,k)
        return res

    def helper(self,ind,ds,res,target,k):
        if(target<0):
            return 0
        if(target==0 and len(ds)==k):
            res.append(ds.copy())
            return 
        #we need numbers from 1 till 10
        for i in range(ind,10):
            ds.append(i)
            self.helper(i+1,ds,res,target-i,k)
            ds.pop()

       