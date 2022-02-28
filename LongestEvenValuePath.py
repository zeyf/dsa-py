class Solution:



    def calcLongest(self, root, visited, rel):
        if not root or (root.val & 1):
            return 0;
        
        mLongestEven = 0;

        if rel[root] and rel[root] not in visited and rel[root].val % 2 == 0:
            visited.add(rel[root]);
            mLongestEven = max(mLongestEven, 1+self.calcLongest(rel[root], visited, rel));
            visited.remove(rel[root]);
        if root.left and root.left not in visited and root.left.val % 2 == 0:
            visited.add(root.left);
            mLongestEven = max(mLongestEven, 1+self.calcLongest(root.left, visited, rel));
            visited.remove(root.left);
        if root.right and root.right not in visited and root.right.val % 2 == 0:
            visited.add(root.right);
            mLongestEven = max(mLongestEven, 1+self.calcLongest(root.right, visited, rel));
            visited.remove(root.right);

        return mLongestEven;

    def solve(self, root):
        if not root:
            return 0;
        
        stack = [(root, None)];
        rel = {  };

        while len(stack):
            c, p = stack.pop();
            rel[c] = p;
            
            if c.right:
                stack.append((c.right, c));
            if c.left:
                stack.append((c.left, c));

        stack = [root];
        m = 0;

        visited = set();
        while len(stack):
            node = stack.pop();

            if (node.val % 2 == 0):
                x = self.calcLongest(node, visited, rel);
                if x == 0:
                    x = 1;
                m = max(m, x);

            if node.right:
                stack.append(node.right);
            if node.left:
                stack.append(node.left);
        return m;
