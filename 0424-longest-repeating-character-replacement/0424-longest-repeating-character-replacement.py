from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap=defaultdict(int)
        maxi=0
        left=0
        for right in range(0,len(s)):
            if s[right] not in hmap:
                hmap[s[right]]=1
            else:
                hmap[s[right]]+=1
            while(right-left+1-max(hmap.values())>k):
                hmap[s[left]]-=1
                if(hmap[s[left]]==0):
                    del hmap[s[left]]
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi
      