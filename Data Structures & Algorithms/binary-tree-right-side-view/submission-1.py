# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque([root])
        while q:
            seenSide = None

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    seenSide = node
                    q.append(node.left)
                    q.append(node.right)
            if seenSide:
                ans.append(seenSide.val)
        return ans
