'''
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        self.sum = 0
        
        def traverseBST(treeNode):
            if treeNode.val >= L and treeNode.val <=R:
                self.sum += treeNode.val
            if treeNode.val > L and treeNode.left:
                traverseBST(treeNode.left)
            if treeNode.val < R and treeNode.right:
                traverseBST(treeNode.right)  
            
        traverseBST(root)
        return self.sum