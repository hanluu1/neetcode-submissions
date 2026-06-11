# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #how to count the node:
         #true if both is null
        if not p and not q:
            return True
        #edge case: return false if either node is null
        if not p or not q:
            return False
        #false if not share the same value
        if p.val != q.val: 
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            