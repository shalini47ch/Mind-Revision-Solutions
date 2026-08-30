class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #we need to evaluate the reverse polish notification using stack
        stack=[]
        for ele in tokens:
            if ele not in "+-*/":
                stack.append(ele)
            else:
                op2=int(stack.pop())
                op1=int(stack.pop())
                if(ele=="+"):
                    stack.append(op1+op2)
                elif(ele=="-"):
                    stack.append(op1-op2)
                elif(ele=="*"):
                    stack.append(op1*op2)
                elif(ele=="/"):
                    stack.append(op1/op2)
        return int(stack[-1])
       