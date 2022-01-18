class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val);

        c = root;
        while True:
            if val < c.val:
                if c.left:
                    c = c.left;
                else:
                    c.left = TreeNode(val);
                    break;
            if val > c.val:
                if c.right:
                    c = c.right;
                else:
                    c.right = TreeNode(val);
                    break;
        return root;