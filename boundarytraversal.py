class Solution:
        
    def findFirstLeaf(self, childparentpair, direction, relationships):
        child, parent = childparentpair;
        if not child:
            return None;
        relationships[child] = parent;
        if not child.left and not child.right:
            return child;
        return self.findFirstLeaf((child.left if direction < 0 else child.right, child), direction, relationships) or self.findFirstLeaf((child.right if direction < 0 else child.left, child), direction, relationships);

    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [];
        elif not root.left and not root.right:
            return [root.val];

        left = [];
        right = [];
        relationships = {  };
        firstLeft = self.findFirstLeaf((root.left, root), -1, relationships);
        firstRight = self.findFirstLeaf((root.right, root), 1, relationships);
        seen = set();
        if firstLeft:
            seen.add(firstLeft);
            while firstLeft is not root:
                left.append(firstLeft.val);
                firstLeft = relationships[firstLeft];
        if firstRight:
            seen.add(firstRight);
            while firstRight is not root:
                right.append(firstRight.val);
                firstRight = relationships[firstRight];
        
        preorder = [root];
        bottom = [];
        while len(preorder):
            node = preorder.pop();
            if not node.left and not node.right and node not in seen:
                bottom.append(node.val);
            if node.right:
                preorder.append(node.right);
            if node.left:
                preorder.append(node.left);
        
        return [root.val] + left[::-1] + bottom + right;