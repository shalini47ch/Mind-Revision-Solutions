from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #here we need to return the length of the longest substring use sliding window +hmap to solve this 
        hmap=defaultdict(int)
        maxi=0
        left=0
        for right in range(0,len(s)):
            if s[right] not in hmap:
                hmap[s[right]]=1
            else:
                hmap[s[right]]+=1
            while(hmap[s[right]]>1):
                hmap[s[left]]-=1
                if(hmap[s[left]]==0):
                    del hmap[s[left]]
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi
        