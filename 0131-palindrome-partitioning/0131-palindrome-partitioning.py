class Solution:
    #here we need to partition the string such that every string is a partition
    def isPalindrome(self,s,start,end):
        return s[start:end+1]==s[start:end+1][::-1]
    
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        res=[]
        self.helper(0,[],res,s,n)
        return res

    def helper(self,ind,ds,res,s,n):
        if(ind==n):
            res.append(ds.copy())
            return 
        #now here we will iterate from ind till length of the string
        for end in range(ind,n):
            if(self.isPalindrome(s,ind,end)):
                ds.append(s[ind:end+1])
                self.helper(end+1,ds,res,s,n)
                #here we need to do the undo operation as well
                ds.pop()
            

                