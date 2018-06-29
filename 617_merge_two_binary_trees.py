# Definition for a binary tree node.
#class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        traversal_length = min(len(t1), len(t2))
        return traversal_length

s = Solution()
print (s.mergeTrees([1,3,2,5], [2,1,3,null,4,null,7]))
