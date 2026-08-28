class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        n=len(candidates)
        self.helper(0,[],res,candidates,target,n)
        return res

    def helper(self,ind,ds,res,candidates,target,n):
        if(target==0):
            res.append(ds.copy())
            return 
        for i in range(ind,n):
            if(candidates[i]<=target):
                ds.append(candidates[i])
                self.helper(i,ds,res,candidates,target-candidates[i],n)
                ds.pop()


        