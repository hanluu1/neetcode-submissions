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
        #one pass
        copyOldNode = defaultdict(lambda: Node(0))
        copyOldNode[None] = None

        cur = head
        while cur:
            copyOldNode[cur].val = cur.val
            copyOldNode[cur].next = copyOldNode[cur.next]
            copyOldNode[cur].random  = copyOldNode[cur.random]
            cur = cur.next
        return copyOldNode[head]


