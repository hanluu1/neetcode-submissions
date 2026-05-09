# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #need to reach to the nth from the end, cut the link that link to the number and connect with the rest
        dummy = ListNode(0,head)
        left = dummy
        right = head 
        #get right pointer reaching nth position
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next #cut the link

        return dummy.next