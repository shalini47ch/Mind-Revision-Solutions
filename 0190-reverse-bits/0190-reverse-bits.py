class Solution:
    def reverseBits(self, n: int) -> int:
        #first convert to binary
        res=bin(n)[2:]
        res=res.zfill(32)
        ans=res[::-1]
        #now at last return the integer
        return int(ans,2)
       

        