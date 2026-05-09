# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #have prev and current node, prev null, curr is head
        prev, curr = None, head
        while curr:
            #have the node that store the value of current node.next so when moving doesnt lost that value
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
