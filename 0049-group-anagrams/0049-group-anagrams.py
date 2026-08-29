from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use hmap to solve this 
        hmap=defaultdict(int)
        for word in strs:
            newword="".join(sorted(word))
            if newword not in hmap:
                hmap[newword]=[word]
            else:
                hmap[newword].append(word)
        ans=[]
        for k,v in hmap.items():
            ans.append(v)
        return ans
        
       