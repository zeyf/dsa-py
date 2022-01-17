class BinarySearchTreeNode:
    def __init__(self, val):
        self.val = val;
        self.left = None;
        self.right = None;
        self.frequency = 1;

class BinarySearchTree:
    def __init__(self):
        self.root = None;
        self.uniqueNodeCount = 0;
    
    def insert(self, val):
        self.root = self.__inserter(val, self.root);

    def __inserter(self, val, root):
        if not root:
            self.uniqueNodeCount += 1;
            return BinarySearchTreeNode(val);
        
        if val > root.val:
            root.right = self.__inserter(val, root.right);
        elif val < root.val:
            root.left = self.__inserter(val, root.left);
        else:
            root.frequency += 1;

        return root;

    def search(self, target):
        return self.__searcher(target, self.root);
    
    def __searcher(self, target, root):
        if not root:
            return None;
        
        if target > root.val:
            return self.__searcher(target, root.right);
        elif target < root.val:
            return self.__searcher(target, root.left);

        return root;

    def size(self):
        return self.uniqueNodeCount;
    
    def empty(self):
        return not self.uniqueNodeCount;
    
    # iterative inorder
    def sort(self):
        values = [];
        stack = [];
        seen = set();
        if self.root:
            stack.append(self.root);
        
        while len(stack):
            current = stack[-1];
            while current and current not in seen:
                seen.add(current);
                current = current.left;
                if current:
                    stack.append(current);

            leftmostnode = stack[-1];
            values.append((leftmostnode.val, leftmostnode.frequency));
            stack.pop();
            if leftmostnode.right:
                stack.append(leftmostnode.right);

        return values;
    
    def copy(self):
        return self.__copier(self.root);

    def __copier(self, root):
        if not root:
            return None;
        node = BinarySearchTreeNode(root.val);
        node.left = self.__copier(root.left);
        node.right = self.__copier(root.right);
        return node;