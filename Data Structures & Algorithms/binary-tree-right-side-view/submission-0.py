# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #only return the node that can see from the right
        #queue idea
        #add node in by levels and append right node to ans
        #pop node out when add new node in
        ans = []
        q = deque([root])
        while q:
            seenSide = None
            qlen = len(q)

            for i in range(qlen):
                #pop elements from the left and add elements from the right
                node = q.popleft()
                if node:
                    seenSide = node 
                    q.append(node.left)
                    q.append(node.right)
            if seenSide:
                ans.append(seenSide.val)
        return ans


