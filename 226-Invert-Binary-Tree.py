'''
Given the root of a binary tree, invert the tree, and return its root.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helperInvert(self, current):
        if (current == None):
            return

        self.helperInvert(current.right)
        self.helperInvert(current.left)

        temp = current.left
        current.left = current.right
        current.right = temp

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helperInvert(root)
        return root
