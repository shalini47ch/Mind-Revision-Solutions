#first create the structure of the node and use the concept of doubly linked list along with helper of remove from end and add to front
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        #now here perform the initialization and then solve
        self.capacity=capacity
        self.cache={}
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    #now create two helpers one is to removefromend and the other is addtofront
    def addtofront(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
    
    #now one more helper to remove from end
    def removefromend(self,node):
        nextnode=node.next
        prevnode=node.prev
        prevnode.next=nextnode
        nextnode.prev=prevnode

    def get(self, key: int) -> int:
        #here we need to return the value of the key
        if key not in self.cache:
            return -1
        #the other case is when it is in the cache
        node=self.cache[key]
        #now next step is to remove from end and add to front
        self.removefromend(node)
        self.addtofront(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        #if the number of keys exceeds the capacity evict the lruele
        if key in self.cache:
            node=self.cache[key]
            node.value=value 
            #now do for remove from end and add to front
            self.removefromend(node)
            self.addtofront(node)
        else:
            newnode=Node(key,value)
            self.cache[key]=newnode
            self.addtofront(newnode)
            #now next is to check for capacity
            if(len(self.cache)>self.capacity):
                lruele=self.tail.prev
                del self.cache[lruele.key]
                self.removefromend(lruele)


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)