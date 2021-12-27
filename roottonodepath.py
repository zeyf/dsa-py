from DS.binarytreenodes import BinaryTreeNode;
from DS.queues import Queue;

# simple recursive solution with backtracking
def rootToNodePath(root, targetvalue, path=[]):
    if not root:
        return [];
    path.append(root.val);
    if root.val == targetvalue:
        return path[::];

    left = rootToNodePath(root.left, targetvalue, path);
    if len(left) > 0:
        path.pop();
        return left;
    right = rootToNodePath(root.right, targetvalue, path);
    path.pop();
    return right;

def rnpathiter(root, targetvalue):
    stack = [];
    if root:
        stack.append((root, None));
    seenMap = {  };
    path = [];
    while len(stack):
        child, parent = stack.pop();
        seenMap[child] = parent;

        if child.val == targetvalue:
            currentchild = child;
            while currentchild:
                path.append(currentchild.val);
                currentchild = seenMap[currentchild];
        #preorder
        if child.right:
            stack.append((child.right, child));
        if child.left:
            stack.append((child.left, child));

    return path[::-1];


root = BinaryTreeNode(1);
root.left = BinaryTreeNode(2);
root.left.left = BinaryTreeNode(0);
root.left.right = BinaryTreeNode(5);
root.right = BinaryTreeNode(50);

print(rnpathiter(root, int(input("Enter the target number for tree:\t"))));
