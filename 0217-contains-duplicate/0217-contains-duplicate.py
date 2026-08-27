from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #here we need to return True or False
        hmap=defaultdict(int)
        for i in range(0,len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]]=1
            else:
                hmap[nums[i]]+=1
        for k,v in hmap.items():
            if(v>1):
                return True
        return False

      