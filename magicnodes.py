from DS.binarytreenodes import BinaryTreeNode;

def canPop(node, seen):
    return True if (not node.left and not node.right) or (not node.left and node.right and node.right in seen) or (not node.right and node.left and node.left in seen) or (node.left and node.left in seen and node.right and node.right in seen) or (node in seen) else False;

def countMagicNodes(root):
    stack = [];
    if root:
        stack.append((root, root.val, 1));
        ##############node,sum,nodecount
    seen = {  };
    magicNodeCount = 0;
    while len(stack):
        current, currentsum, currentnodecount = stack[-1];
        while current and current not in seen:
            seen[current] = (current, current.val, 1);
            if current.right:
                stack.append((current.right, current.right.val, 1));
            current = current.left;
            if current:
                stack.append((current, current.val, 1));

        if canPop(stack[-1][0], seen):
            node, nodesum, nodecount = stack[-1];
            if node.left and node.left in seen:
                nodesum += seen[node.left][1];
                nodecount += seen[node.left][2];
            if node.right and node.right in seen:
                nodesum += seen[node.right][1];
                nodecount += seen[node.right][2];
            
            stack.pop();
            seen[node] = (node, nodesum, nodecount);
            popnode, popsum, popcount = seen[node];
            if (popnode.left and popnode.right) and ((seen[popnode.left][2] % 2 == 1 and  seen[popnode.right][2] % 2 == 0) or (seen[popnode.left][1] % 2 == 0 and seen[popnode.right][1] % 2 == 1)):
                magicNodeCount += 1;
                print("MAGIC NODE #{} DATA: ({}, {}, {})\t".format(magicNodeCount, popnode.val, popsum, popcount));
        
    return magicNodeCount;

'''
from amazon:

Given a binary tree, count the total number of magic parents,
where a node which is not NULL and has both left and right children
and the sum of the number of nodes in the left subtree is odd and that
of right subtree is even (or sum of nodes in the left subtree as even and right subtree as odd)
should be considered as a magic parent. Node 1 is always the Root node
'''

root = BinaryTreeNode(100);
root.left = BinaryTreeNode(50);
root.left.left = BinaryTreeNode(25);
root.left.left.right = BinaryTreeNode(40);
root.left.left.right.left = BinaryTreeNode(35);
root.left.left.right.left.left = BinaryTreeNode(30);
root.right = BinaryTreeNode(200);
#root.right.left = BinaryTreeNode(150);
root.right.right = BinaryTreeNode(500);

print("NUMBER OF MAGIC NODES:\t", countMagicNodes(root));
