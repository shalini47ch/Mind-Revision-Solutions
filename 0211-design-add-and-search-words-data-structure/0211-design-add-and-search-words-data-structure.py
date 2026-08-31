#this is based on the concept of trie with dfs 
class Node:
    def __init__(self):
        self.links=[None for i in range(26)]
        self.flag=False
    
    def containsKey(self,ch):
        return self.links[ord(ch)-ord("a")]!=None
    
    def put(self,ch):
        self.links[ord(ch)-ord("a")]=Node()
    
    def get(self,ch):
        return self.links[ord(ch)-ord("a")]
    
    def setEnd(self):
        self.flag=True 
    
    def isEnd(self):
        return self.flag

class WordDictionary:
    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        #same like add word as we do in trie
        node=self.root
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i])
            node=node.get(word[i])
        node.setEnd()
        
    def search(self, word: str) -> bool:
        return self.dfs(self.root,word,0)
    
    #now create a helper function to perform dfs
    def dfs(self,node,word,ind):
        if(ind==len(word)):
            return node.isEnd()
        ch=word[ind]
        if(ch=="."):
            #means we need to do dfs on all the children
            for child in node.links:
                if child:
                    if(self.dfs(child,word,ind+1)):
                        return True
            return False
        if not node.containsKey(ch):
            return False
        node=node.get(word[ind])
        return self.dfs(node,word,ind+1)



        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)