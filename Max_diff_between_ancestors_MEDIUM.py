# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# # A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.tree_min_max(root,root.val,root.val)

    def tree_min_max(self,node,mn,mx):
        if not node:
            return mx - mn
        mn = min(mn,node.val)
        mx = max(mx,node.val)

        left_diff = self.tree_min_max(node.left,mn,mx)
        right_diff = self.tree_min_max(node.right,mn,mx)

        return max(left_diff,right_diff)
#the tree_min_max function takes the max and min value till that point in the tree,compares with current node value 
  
