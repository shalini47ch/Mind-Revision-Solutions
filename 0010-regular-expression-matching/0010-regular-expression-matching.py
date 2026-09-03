class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #. matches with single character and * means zero or more characters
        return self.helper(0,0,s,p)

    def helper(self,i,j,s,p):
        if(j==len(p)):
            return i==len(s)
        #now lets first do for first match
        firstmatch=(i<len(s) and (s[i]==p[j] or p[j]=="."))
        if(j+1<len(p) and p[j+1]=="*"):
            #now there are two options either to pick or notpick
            notpick=self.helper(i,j+2,s,p)
            pick=firstmatch and self.helper(i+1,j,s,p)
            #here we will return pick or notpick
            return (pick or notpick)
        else:
            return firstmatch and self.helper(i+1,j+1,s,p)






    
    


       