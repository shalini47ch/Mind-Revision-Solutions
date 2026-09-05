# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #here we will use the concept of k way merge to solve this we need the minimum from each of the lists in the list so use minheap
        minheap=[]
        for ind,node in enumerate(lists):
            if node:
                heapq.heappush(minheap,[node.val,ind,node])
        dummy=ListNode(-1)
        curr=dummy
        #now keep iterating while length of minheap is greater than 0
        while(len(minheap)>0):
            val,indi,node=heapq.heappop(minheap)
            #node here is basically the next node
            curr.next=node
            curr=curr.next
            if node.next:
                heapq.heappush(minheap,[node.next.val,indi,node.next])
        #now at last we return dummy.next
        return dummy.next 
       