from DS.binarytreenodes import BinaryTreeNode;
from DS.queues import Queue;

def diameterOfFullTree(root):
    if not root:
        return 0;

    minoffset = 1000000;
    maxoffset = -1000000;
    q = Queue();
    q.enqueue((root, 0));

    while not q.empty():
        node, offset = q.dequeue();
        if offset > maxoffset:
            maxoffset = offset;
        if offset < minoffset:
            minoffset = offset;
        if node.left:
            q.enqueue((node.left, offset - 1));
        if node.right:
            q.enqueue((node.right, offset + 1));
    
    return abs(minoffset - maxoffset) + 1;

root = BinaryTreeNode(50);
root.left = BinaryTreeNode(40);
root.right = BinaryTreeNode(60);
root.left.left = BinaryTreeNode(30);
root.left.right = BinaryTreeNode(45);
root.left.right.left = BinaryTreeNode(44);
root.left.right.left.left = BinaryTreeNode(43);
root.left.right.left.left.left = BinaryTreeNode(42);
root.left.right.left.left.left.left = BinaryTreeNode(41);
root.right.right = BinaryTreeNode(80);
root.right.right.left = BinaryTreeNode(75);


print("FULL TREE DIAMETER: ", diameterOfFullTree(root));
'''
                    50
                40      60
            30      45      80
                44      75
            43
        42
    41

    1   2   3   4   5   6   7
'''