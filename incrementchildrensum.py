def sumUp(root):
    if not root or (not root.left and not root.right):
        return;
    sumUp(root.left);
    sumUp(root.right);
    root.val = (0 if not root.left else root.left.val) + (0 if not root.right else root.right.val);

def checkChildrenSum(root):
    if not root or (not root.left and not root.right):
        return True;
    subtreeresult = checkChildrenSum(root.left) and checkChildrenSum(root.right);
    leftrightsum = (0 if not root.left else root.left.val) + (0 if not root.right else root.right.val);
    return subres and leftrightsum == root.val;

def changeChildrenSum(root):
    if not root or checkChildrenSum(root):
        return;

    relationships = {  };
    leaves = [];
    stack = [(root, None)];
    while len(stack):
        child, parent = stack.pop();
        relationships[child] = parent;
        if not child.left and not child.right:
            leaves.append(child);
        if child.right:
            stack.append((child.right, child));
        if child.left:
            stack.append((child.left, child));
    
    for leaf in leaves:
        current, maxValueNode = leaf, leaf;
        while current:
            if current.val > maxValueNode.val:
                maxValueNode = current;
                current = relationships[current];
        
        temp = leaf.val;
        leaf.val = maxValueNode.val;
        maxValueNode.val = temp;
    
    sumUp(root);