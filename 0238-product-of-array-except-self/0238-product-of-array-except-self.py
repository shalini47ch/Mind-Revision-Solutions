class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[0 for i in range(n)]
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i]
        suffix=[0 for i in range(n)]
        suffix[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i]
        ans=[]
        for i in range(0,n):
            if(i==0):
                ans.append(suffix[i+1])
            elif(i==n-1):
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1]*suffix[i+1])
        return ans
        