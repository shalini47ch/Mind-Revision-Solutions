from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=Counter(s)
        y=Counter(t)
        return x==y

        