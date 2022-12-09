class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node): #time: O(n), space: O(n)
            if not node:
                return 0
            dfs(node.right)
            node.val += dfs.sum
            dfs.sum = node.val
            dfs(node.left)
            
        dfs.sum = 0
        dfs(root)
        return root
#--------------------------------------------------------------
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sumOfValues = 0
        def traversal(node): #time: O(n), space: O(n)
            if not node:
                return
            nonlocal sumOfValues

            traversal(node.right)

            temp = node.val
            node.val += sumOfValues
            sumOfValues += temp
            
            traversal(node.left)

        traversal(root)
        return root