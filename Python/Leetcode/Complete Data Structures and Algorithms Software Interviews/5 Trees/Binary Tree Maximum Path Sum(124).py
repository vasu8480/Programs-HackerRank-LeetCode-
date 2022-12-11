class Solution:
    answer = -float("inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.answer
    
    def dfs(self,node): #time: O(n), space: O(n)
        if node is None:
            return 0
        
        left = self.dfs(node.left) 
        right = self.dfs(node.right)
        
        left = max(left,0)
        right = max(right,0)
        
        self.answer = max(self.answer,node.val+left+right)
        
        return node.val + max(left,right)
#-------------------------------------------------------------
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf') 
        self.dfs(root)
        return self.max_sum

    def dfs(self, node): #time: O(n), space: O(n)
        if not node:
            return 0
        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)
        self.max_sum = max(self.max_sum, node.val + left + right)
        return node.val + max(left, right)

