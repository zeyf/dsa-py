from DS.binarytreenodes import BinaryTreeNode;

def childrenSumProperty(root):
    if not root or (not root.left and not root.right):
        return True;
    subres = childrenSumProperty(root.left) and childrenSumProperty(root.right);
    leftrightsum = 0;
    if root.left:
        leftrightsum += root.left.val;
    if root.right:
        leftrightsum += root.right.val;
    return subres and leftrightsum == root.val;

root = BinaryTreeNode(45);
root.left = BinaryTreeNode(35);
root.right = BinaryTreeNode(10);
root.right.right = BinaryTreeNode(0);
root.right.left = BinaryTreeNode(10);
root.left.left = BinaryTreeNode(30);
root.left.right = BinaryTreeNode(5);

print(childrenSumProperty(root));