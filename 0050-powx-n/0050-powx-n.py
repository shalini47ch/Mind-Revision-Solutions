class Solution:
    def myPow(self, x: float, n: int) -> float:
        #use the concept of recursion to solve this 
        if(n==0):
            return 1
        if(n<0):
            x=1/x
            n=-n
        ans=self.myPow(x,n//2)
        if(n%2==1):
            return x*ans*ans
        return ans*ans
        