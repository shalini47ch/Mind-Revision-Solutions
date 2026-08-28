# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #here we need to add two numbers represented as linked lists 
        dummy=ListNode(-1)
        tail=dummy
        carry=0
        while(l1!=None or l2!=None or carry):
            su=0
            if(l1!=None):
                su+=l1.val
                l1=l1.next
            if(l2!=None):
                su+=l2.val
                l2=l2.next
            su+=carry
            carry=su//10
            newnode=ListNode(su%10)
            tail.next=newnode
            tail=tail.next
        return dummy.next
       