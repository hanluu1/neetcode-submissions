# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totalN = 0
        curr = head
        while curr:
            totalN += 1 
            curr = curr.next
        #find the index that need to be removed
        removedIndex = totalN - n
        if removedIndex == 0:
            return head.next
        
        cur = head
        for i in range(totalN - 1):
            if i + 1 == removedIndex:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head




        