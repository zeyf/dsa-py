# https://binarysearch.com/problems/Lowest-Common-Ancestor-of-List-of-Values

class Solution:
    def solve(self, root, values):
        if not root:
            return root;
        
        searchset = set();
        for val in values:
            searchset.add(val);
        
        stack = [(root, None)];
        rel = {  };
        targetNodes = [];

        while len(stack):
            child, parent = stack.pop();
            rel[child] = parent;

            if child.val in searchset:
                targetNodes.append(child);
            if child.right:
                stack.append((child.right, child));
            if child.left:
                stack.append((child.left, child));
        
        colormap = {  };

        res = None;
        for node in targetNodes:
            while node:
                if node not in colormap:
                    colormap[node] = 1;
                else:
                    colormap[node] += 1;
                
                if colormap[node] == len(values):
                    return node;
                node = rel[node];

