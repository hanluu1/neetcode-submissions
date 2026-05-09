# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #two list is already sorted
        #have the dummy node is the start
        dummy = node = ListNode()
        while list1 and list2:
        #compare the value in the list one by one
            if list1.val < list2.val:
                node.next = list1
                #update pointer to the next
                list1 = list1.next
            else:
                node.next = list2
                list2= list2.next
            node = node.next
        #if either list is out of value first then the list will link with the left over value of the other list
        node.next = list1 or list2
        return dummy.next