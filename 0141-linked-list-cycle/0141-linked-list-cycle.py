# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #use floyd cycle detection algo to solve this 
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            #move slow by one step and fast by two steps 
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False
        