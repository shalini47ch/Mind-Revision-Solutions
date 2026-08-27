class Solution:
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=n
        while(True):
            slow=self.findsumofsquares(slow)
            fast=self.findsumofsquares(self.findsumofsquares(fast))
            if(slow!=fast):
                continue
            else:
                break
        return (slow==1 and fast==1)

    def findsumofsquares(self,num):
        su=0
        while(num>0):
            digits=num%10
            su=su+(digits*digits)
            num=num//10
        return su
        