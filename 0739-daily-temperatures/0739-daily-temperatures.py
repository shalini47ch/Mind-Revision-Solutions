class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #here we need to return the no of days you have to wait to get warmer temperature so use nearest greater to right logic
        stack=[]
        n=len(temperatures)
        res=[]
        for i in range(n-1,-1,-1):
            while(stack and temperatures[stack[-1]]<=temperatures[i]):
                stack.pop()
            if(len(stack)==0):
                res.append(0)
            else:
                res.append(stack[-1]-i)
            stack.append(i)
        return res[::-1]
        