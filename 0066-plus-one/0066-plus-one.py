class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        #traverse through digits
        for i in range(0,len(digits)):
            num=num*10+digits[i]
        num+=1
        return [int(x) for x in str(num)]
        
            
            
            