# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #when the node at nth node get the next connect to the next of the node
        lenNode = 0
        curr = head
        while curr:
            #count how many node in the list
            lenNode += 1
            curr = curr.next
        #find where the node to delete would be located at?
        deleteAt = lenNode - n

        if deleteAt == 0:
            return head.next

        curr = head
        for i in range(lenNode - 1):
            if (i + 1) == deleteAt:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
        