class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        relationships = {  };
        self.mapRelationships(root, p.val, relationships);
        self.mapRelationships(root, q.val, relationships);
        seen = set();
        while p:
            seen.add(p);
            p = relationships[p];
        while q:
            if q in seen:
                return q;
            q = relationships[q];
    
    def mapRelationships(self, root, key, relationships):
        child, parent = root, None;
        
        while True:
            relationships[child] = parent;
            if key < child.val:
                parent = child;
                child = child.left;
            elif key > child.val:
                parent = child;
                child = child.right;
            else:
                break;