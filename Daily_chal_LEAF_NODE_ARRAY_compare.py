# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# ques = Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree_array(self,node,arr):
        if node is not None:
            if node.left is None and node.right is None:
                arr.append(node.val)
            self.tree_array(node.left,arr)
            self.tree_array(node.right,arr)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        arr1,arr2 = [],[]
        self.tree_array(root1,arr1)
        self.tree_array(root2,arr2)
        if len(arr1) != len(arr2):
            return False
        else:    
            for i in range(len(arr1)):
                if arr1[i]!=arr2[i]:
                    return False
            return True    

#can be done in a better way looking for better complexity
            
    
