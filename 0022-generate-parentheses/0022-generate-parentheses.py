class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #use the recursion+backtrack to solve this 
        res=[]
        self.helper(0,0,"",res,n)
        return res

    def helper(self,op,cl,s,res,n):
        if(op==n and cl==n):
            res.append(s)
            return 
        if(op<n):
            self.helper(op+1,cl,s+"(",res,n)
        if(op>cl):
            self.helper(op,cl+1,s+")",res,n)
        
        