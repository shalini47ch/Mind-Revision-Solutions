# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #here we will use the logic of reverse and middle and then perform the connections to solve this 
        #first handle the edge case
        if head is None or head.next is None:
            return 
        mid=self.middle(head)
        newhead=self.reverse(mid.next)
        mid.next=None
        c1=head
        c2=newhead
        while(c1!=None and c2!=None):
            f1=c1.next
            f2=c2.next
            #now perform the connections 
            c1.next=c2
            c2.next=f1
            c1=f1
            c2=f2

    def reverse(self,head):
        prev=None
        curr=head
        while(curr!=None):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    
    #now create a helper to find the middle of the linked list
    def middle(self,head):
        #use the concept of fast and slow pointer to solve this 
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            #move slow by one step and fast by two steps
            slow=slow.next
            fast=fast.next.next
        return slow 
       