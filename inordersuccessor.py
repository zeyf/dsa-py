from DS.binarysearchtrees import *;

def inorderSuccessor(root:BinarySearchTreeNode, p:BinarySearchTreeNode)->BinarySearchTreeNode:
    if p.right:
        c = p.right;
        while c.left:
            c = c.left;
        return c;
        
    stack = [(root, None, 0)];
    relationships = {  };
    while len(stack):
        child, parent, sideFrom = stack.pop();
        relationships[child] = (parent, sideFrom);
        if p.val < child.val and child.left:
            stack.append((child.left, child, -1));
        elif p.val > child.val and child.right:
            stack.append((child.right, child, 1));
        elif p.val == child.val:
            stack.append(child);
            break;

    if not len(stack):
        return None;
        
    current = stack.pop();
    while current and relationships[current][1] >= 0:
        current = relationships[current][0];
    if not current:
        return current;
    return relationships[current][0];

def inorderSuccessor2(root: BinarySearchTreeNode, p: BinarySearchTreeNode) -> BinarySearchTreeNode:
    if p.right:
        c = p.right;
        while c.left:
            c = c.left;
        return c;

    c = root;
    lastLeftChildParent = None;
    while c:
        if p.val > c.val:
            c = c.right;
        elif p.val < c.val:
            lastLeftChildParent = c;
            c = c.left;
        elif p.val == c.val:
            break;
    return lastLeftChildParent;

bst = BinarySearchTree();
bst.insert(100);
bst.insert(50);
bst.insert(70);
bst.insert(75);
bst.insert(75);
bst.insert(40);
bst.insert(110);
bst.insert(120);
bst.insert(105);
bst.insert(104);
bst.insert(103);
bst.insert(102);

copy = bst.copy();
print(bst.sort());
res1 = inorderSuccessor2(copy, bst.search(75));
if res1:
    print(res1.val);
else:
    print(None);