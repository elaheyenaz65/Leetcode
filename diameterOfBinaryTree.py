# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def nodeDiameter(node, res):
            if node is None: return 0
            ldim=nodeDiameter(node.left, res)
            rdim=nodeDiameter(node.right, res)
            # if root.left is None and root.right is None: return 0
            res[0] =max(ldim+rdim, res[0])
            return max(ldim ,rdim)+1
        res1=[0] 
        nodeDiameter(root, res1)
        # print (root.val)
        # print(maxl, temp)
        # maxl=max(maxl,temp)
        return res1[0]
