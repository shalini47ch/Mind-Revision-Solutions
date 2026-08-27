class Solution:
    def countBits(self, n: int) -> List[int]:
        #count set bits 
        ans=[0 for i in range(n+1)]
        for i in range(0,n+1):
            ele=self.countbits(i)
            ans[i]=ele
        return ans

    def countbits(self,num):
        count=0
        while(num>0):
            count+=1
            num=num&(num-1)
        return count