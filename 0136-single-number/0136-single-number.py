from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #brute way is by using hmap and optimal way is by using xor
        xor=0
        for ele in nums:
            xor=xor^ele
        return xor 




        # hmap=defaultdict(int)
        # for i in range(0,len(nums)):
        #     if nums[i] not in hmap:
        #         hmap[nums[i]]=1
        #     else:
        #         hmap[nums[i]]+=1
        # for k,v in hmap.items():
        #     if(v==1):
        #         return k

        
        