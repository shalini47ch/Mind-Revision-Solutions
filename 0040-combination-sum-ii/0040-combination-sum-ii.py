class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        candidates.sort()
        res=[]
        self.helper(0,[],candidates,res,target,n)
        return res

    def helper(self,ind,ds,candidates,res,target,n):
        if(target==0):
            res.append(ds.copy())
            return 
        for i in range(ind,n):
            if(i>ind and candidates[i]==candidates[i-1]):
                continue
            if(candidates[i]>target):
                break
            ds.append(candidates[i])
            self.helper(i+1,ds,candidates,res,target-candidates[i],n)
            ds.pop()


        