from DS.binarytreenodes import *;

def findMaxDistance(node, relationships, seen):
    maxDist = 0;

    if node in relationships and relationships[node] and relationships[node] not in seen:
        seen.add(relationships[node]);
        maxDist = max( maxDist, 1 + findMaxDistance(relationships[node], relationships, seen) );
    if node.left and node.left not in seen:
        seen.add(node.left);
        maxDist = max( maxDist, 1 + findMaxDistance(node.left, relationships, seen) );
    if node.right and node.right not in seen:
        seen.add(node.right);
        maxDist = max( maxDist, 1 + findMaxDistance(node.right, relationships, seen) );

    return maxDist;

def distance(childparentpair, relationships, seen, targetValue):
    child, parent = childparentpair;
    if not child:
        return 0;
    relationships[child] = parent;
    if child.val == targetValue:
        seen.add(child);
        return findMaxDistance(child, relationships, seen);
    return max( distance((child.left, child), relationships, seen, targetValue), distance((child.right, child), relationships, seen, targetValue) );

def timeToBurnTree(root, startValue):
    if not root:
        return 0;
    relationships, seen = {  }, set();
    return distance((root, None), relationships, seen, startValue);





root = BinaryTreeNode(1);
root.left = BinaryTreeNode(2);
root.right = BinaryTreeNode(3);
root.right.left = BinaryTreeNode(4);
root.right.right = BinaryTreeNode(5);
root.right.right.right = BinaryTreeNode(6);
root.right.right.right.left = BinaryTreeNode(7);
root.right.right.right.right = BinaryTreeNode(8);

print("TREE 1:");
print(timeToBurnTree(root, 5)); # prints 3
print(timeToBurnTree(root, 2)); # prints 5
print(timeToBurnTree(root, 1)); # prints 4
print(timeToBurnTree(root, 4)); # prints 4

root2 = BinaryTreeNode(1);
root2.right = BinaryTreeNode(2);
root2.right.right = BinaryTreeNode(3);
root2.right.right.right = BinaryTreeNode(4);
root2.right.right.right.right = BinaryTreeNode(5);

print("TREE 2:", timeToBurnTree(root2, 3)); # prints 2