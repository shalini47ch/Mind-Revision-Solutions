from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force way is to run two loops and optimal way is to use hmap to solve this 
        hmap=defaultdict(int)
        for i in range(0,len(nums)):
            if target-nums[i] in hmap:
                return [i,hmap[target-nums[i]]]
            hmap[nums[i]]=i
        return [-1,-1]

       