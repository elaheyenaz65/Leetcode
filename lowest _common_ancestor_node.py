# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if  root is None : return
        res=root
        found=0
        
        while 1:
            print(res.val)
            if (p.val<=res.val and q.val>=res.val ) or (p.val>=res.val and q.val<=res.val) :
                found=1
                return res
            if p.val<=res.val and q.val<=res.val: res=res.left
            else:
                res=res.right
        
        # if((p.val <= root.val  and q.val >=  root.val ) or (p.val>=root.val and q.val<= root.val)): return root
        # if (p.val< root.val and q.val< root.val): return self.lowestCommonAncestor(root.left, p,q)
        # return self.lowestCommonAncestor(root.right,p,q)

        

        
