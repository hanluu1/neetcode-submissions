# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #dummy pointer 
        dummy = ListNode(0, head)
        
        #need to reach node at position left 
        beforeLeft, cur = dummy, head
        for i in range(left-1):
            beforeLeft, cur = cur, cur.next  
        
        #change the link of the node from left to right
        prev = None #previous node is the node before left
        for i in range(right - left +1):
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        
        #update pointers from before left and after right
        beforeLeft.next.next = cur
        beforeLeft.next = prev
        return dummy.next