# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #divide the list to 2 using fast and slow pointer
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #2 pointer one point at the beginning of the first list
        #second half of the list
        second = slow.next
        #reverse second half of the list
        prev = slow.next = None
        while second:
            tmp = second.next     #have the temp value to store the value before breaking the link
            second.next = prev
            prev = second
            second = tmp
        #merge 2 half of list   
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


