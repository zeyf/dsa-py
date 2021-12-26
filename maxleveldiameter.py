from DS.binarytreenodes import BinaryTreeNode;
from DS.queues import Queue;

def maxLevelDiameter(root):
    if not root:
        return 0;
    
    maxleveldiameter = -1;
    q = Queue();
    q.enqueue((root, 0));
    while not q.empty():
        size = q.size();
        if abs(q.front()[1] - q.tail()[1]) + 1 > maxleveldiameter:
            maxleveldiameter = abs(q.front()[1] - q.tail()[1]) + 1;
        while size:
            node, offset = q.dequeue();
            if node.left:
                q.enqueue((node.left, offset - 1));
            if node.right:
                q.enqueue((node.right, offset + 1));
            size -= 1;

    return maxleveldiameter;


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

print("MAX LEVEL DIAMETER:\t", maxLevelDiameter(root));

'''
                    50 ===> 1
                40      60 ===> 3
            30      45      80 ===> 5 max level diameter
                44      75 ===> 3
            43 ===> 1
        42 ===> 1
    41 ===> 1

    1   2   3   4   5   6   7
'''