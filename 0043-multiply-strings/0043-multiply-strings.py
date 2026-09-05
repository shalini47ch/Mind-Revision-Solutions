class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if(num1=="0" or num2=="0"):
            return "0"
        m=len(num1)
        n=len(num2)
        res=[0 for i in range(m+n)]
        #now iterate in reverse order
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                #lets first find the digit of nums
                digit1=ord(num1[i])-ord("0")
                digit2=ord(num2[j])-ord("0")
                product=digit1*digit2
                pos=i+j+1
                res[pos]+=product
                #handle carry
                res[pos-1]+=res[pos]//10
                res[pos]=res[pos]%10
        #now the next step is to handle the leading zeroes
        start=0
        while(start<len(res) and res[start]==0):
            start+=1
        #now at last we need to return the result here trailing ones are also handled
        return "".join(str(x) for x in res[start:])


        
        