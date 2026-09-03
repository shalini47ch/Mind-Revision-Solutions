from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #use sliding window+hmap to solve this 
        hmap1=defaultdict(int)
        hmap2=defaultdict(int)
        res=""
        for i in range(0,len(t)):
            hmap2[t[i]]+=1
        desiredcount=len(t)
        matchcount=0
        i=0
        j=0
        while(True):
            flag1=False
            flag2=False
            while(i<len(s) and matchcount<desiredcount):
                hmap1[s[i]]+=1
                #if the hmap1[s[i]]<=hmap2[s[i]] means we can increase the matchcount 
                if(hmap1[s[i]]<=hmap2[s[i]]):
                    matchcount+=1
                flag1=True
                i+=1
            #now the next step is to acquire and release
            while(j<i and matchcount==desiredcount):
                pans=s[j:i]
                if(res=="" or len(pans)<len(res)):
                    res=pans
                hmap1[s[j]]-=1
                if(hmap1[s[j]]<hmap2[s[j]]):
                    matchcount-=1
                if(hmap1[s[j]]==0):
                    del hmap1[s[j]]
                flag2=True
                j+=1
            if(not flag1 and not flag2):
                break
        return res
            



       