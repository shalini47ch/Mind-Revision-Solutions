from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #here we need to return the list of size of all parts 
        #first we will use hmap to solve this and then use partitions 
        hmap=defaultdict(int)
        for i in range(0,len(s)):
            hmap[s[i]]=i
        start=0
        end=0
        res=[]
        #now traverse through the given string
        for ind,ch in enumerate(s):
            end=max(end,hmap[ch])
            if(ind==end):
                #here we need to add the sizes to the results
                res.append(end-start+1)
                start=ind+1
        return res