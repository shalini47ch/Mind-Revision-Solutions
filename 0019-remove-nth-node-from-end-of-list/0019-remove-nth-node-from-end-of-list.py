# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #lets move the fast pointer will the nth position and then move to slow and fast and then perform connection
        dummy=ListNode(-1)
        dummy.next=head
        slow=dummy
        fast=dummy
        for i in range(0,n+1):
            fast=fast.next
        while(fast!=None):
            #move slow by one step and fast step
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next
        