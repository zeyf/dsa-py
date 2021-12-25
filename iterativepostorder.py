from DS.binarytreenodes import BinaryTreeNode;

def recursivePostorder(root):
    if not root:
        return stack;
    recursivePostorder(root.left);
    recursivePostorder(root.right);
    print(root.val);
    return stack;

def isLeaf(node):
    return True if not node.left and not node.right else False;

def leftSeen(node, seen):
    return True if node.left and node.left in seen else False;

def rightSeen(node, seen):
    return True if node.right and node.right in seen else False;

def noRightWithLeftSeen(node, seen):
    return True if not node.right and leftSeen(node, seen) else False;

def noLeftWithRightSeen(node, seen):
    return True if not node.left and rightSeen(node, seen) else False;

def bothLeftSeenAndRightSeen(node, seen):
    return True if node.left and leftSeen(node, seen) and node.right and rightSeen(node, seen) else False;

def iterativePostorder(root):
    stack = [];
    if root:
        stack.append(root);

    seen = set();
    while len(stack):
        current = stack[-1];
        while current and current not in seen:
            seen.add(current);
            if current.right:
                stack.append(current.right);
            current = current.left;
            if current:
                stack.append(current);
        top = stack[-1];
        if isLeaf(top) or noLeftWithRightSeen(top, seen) or noRightWithLeftSeen(top, seen) or bothLeftSeenAndRightSeen(top, seen) or top in seen:
            print(stack.pop().val);
