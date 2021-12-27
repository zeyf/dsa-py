from DS.binarytreenodes import BinaryTreeNode;

def lowestCommonAncestor(root, descendant1, descendant2):
    stack = [];
    if root:
        stack.append((root, None));

    seenMap = {  };
    while len(stack):
        child, parent = stack.pop();
        seenMap[child] = parent;
        if child.right:
            stack.append((child.right, child));
        if child.left:
            stack.append((child.left, child));
    
    descendant1Map = { };
    d1 = descendant1;
    while d1:
        descendant1Map[d1] = seenMap[d1];
        d1 = seenMap[d1];
    d2 = descendant2;
    res = None;
    while d2:
        if d2 in descendant1Map:
            res = d2;
            break;
        d2 = seenMap[d2];
    
    return res;

'''
root = BinaryTreeNode(50);
root.left = BinaryTreeNode(40);
root.right = BinaryTreeNode(60);
root.left.left = BinaryTreeNode(30);
root.right.right = BinaryTreeNode(70);
root.right.left = BinaryTreeNode(55);
root.right.right.right = BinaryTreeNode(80);


                            50
                          /    \
                        40      60
                      /        /   \
                    30      55      70
                                      \
                                        80

print(lowestCommonAncestor(root, root, root.right.left));
'''