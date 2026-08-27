class Solution:
    def isValid(self, s: str) -> bool:
        #use the concept of stacks to solve this 
        hmap={")":"(","]":"[","}":"{"}
        stack=[]
        #traverse through the given s
        for ch in s:
            if ch in hmap:
                if not stack or stack[-1]!=hmap[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)==0