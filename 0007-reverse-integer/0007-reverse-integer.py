class Solution:
    def reverse(self, x: int) -> int:
        num=x
        sign=1
        if(num<0):
            num=-num
            sign=-1
        rev=0
        while(num>0):
            digits=num%10
            rev=rev*10+digits
            num=num//10
        return 0 if rev>=2**31 else (rev*sign)

   
        
        