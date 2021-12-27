from DS.binarytreenodes import BinaryTreeNode;

def allRootToLeafPaths(root, path="", paths=[]):
    if not root:
        return paths;
    path += str(root.val);
    if not root.left and not root.right:
        paths.append(path);
        return paths;
    path += "->";
    allRootToLeafPaths(root.left, path, paths);
    allRootToLeafPaths(root.right, path, paths);
    return paths;

def allRootToLeafPathsIterative(root):
    stack = [];
    if root:
        stack.append((root, None));
    paths = [];
    seenMap = {  };
    while len(stack):
        child, parent = stack.pop();
        seenMap[child] = parent;
        
        if not child.left and not child.right:
            currentchild = child;
            path = [];
            pathstr = "";
            while currentchild:
                path.append(currentchild.val);
                currentchild = seenMap[currentchild];
            for i in range(len(path) - 1, -1, -1):
                pathstr += str(path[i]);
                if i > 0:
                    pathstr += "->";
            paths.append(pathstr);
        #preorder
        if child.right:
            stack.append((child.right, child));
        if child.left:
            stack.append((child.left, child));
    
    return paths;

root = BinaryTreeNode(1);
root.left = BinaryTreeNode(2);
root.right = BinaryTreeNode(3);
root.left.right = BinaryTreeNode(5);

print(allRootToLeafPathsIterative(root));