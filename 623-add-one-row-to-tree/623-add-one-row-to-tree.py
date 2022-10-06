# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        # edge case if depth is 1 then create a treeNode of val and point treeNode.left to root
        # return treeNode
        if depth == 1:
            Node = TreeNode(val)
            Node.left = root
            return Node
        
        # DFS funtion to add the value at depth
        def DFS(root, d):
            
            # base case if not root return None
            if not root: return None
            
            # call the funtion recursively on left and right sub tree
            left = DFS(root.left, d + 1)
            right = DFS(root.right, d + 1)
            
            # check if current depth is 1 less then the depth at which new node is to be added
            # if yes then create TreeNode of val and point root.left and right to treeNode
            # then point treeNode left and right to left and right sub tree
            if d == (depth - 1):
                root.left = TreeNode(val)
                root.right = TreeNode(val)
            
                root.left.left = left
                root.right.right = right
            
            # return the root
            return root
        
        # call the funtion and return the root value
        return DFS(root,1)