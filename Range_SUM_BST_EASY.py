# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
class Solution(object):
        def inorderTraver(self,node,low,high,sum):
            if node is not None:
                self.inorderTraver(node.left,low,high,sum)
                if low <= node.val <= high:
                    sum[0] += node.val
                self.inorderTraver(node.right, low, high, sum) 

        def rangeSumBST(self, root, low, high):
            sum = [0]
            self.inorderTraver(root, low, high, sum)
            return sum[0]
#uses the concept of tree traversal . using inorder traverse to the left most check if it is in range we want, if yes then add to sum other wise go right accordingly.
#uses recursion.
#the time complexity for the same is O(n)
