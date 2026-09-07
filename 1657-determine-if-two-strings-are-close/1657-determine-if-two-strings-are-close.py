class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #use hmaps and sets to solve this 
        freq1=Counter(word1)
        freq2=Counter(word2)
        s1=set(word1)
        s2=set(word2)
        a1=sorted(freq1.values())
        a2=sorted(freq2.values())
        if(a1==a2 and s1==s2):
            return True
        return False
        