"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #create copy of each node
        #using hash map
        copyOldNode = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val) #copied of nodes
            copyOldNode[cur] = copy 
            cur = cur.next

        #pointer connecting
        cur = head
        while cur:
            copy = copyOldNode[cur] 
            copy.next = copyOldNode[cur.next]
            copy.random = copyOldNode[cur.random]
            cur = cur.next
        
        return copyOldNode[head]