class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #use the concept of hmap+backtracking to solve this 
        n=len(digits)
        res=[]
        if(len(digits)==0):
            return []
        hmap=defaultdict(int)
        hmap["2"]="abc"
        hmap["3"]="def"
        hmap["4"]="ghi"
        hmap["5"]="jkl"
        hmap["6"]="mno"
        hmap["7"]="pqrs"
        hmap["8"]="tuv"
        hmap["9"]="wxyz"
        self.helper(0,"",res,digits,n,hmap)
        return res 
    
    def helper(self,ind,ds,res,digits,n,hmap):
        if(ind>=n):
            res.append(ds)
            return 
        ch=digits[ind]
        currch=hmap[ch]
        #now iterate through the currch
        for i in range(0,len(currch)):
            ds+=currch[i]
            self.helper(ind+1,ds,res,digits,n,hmap)
            ds=ds[:-1]
        

    
      