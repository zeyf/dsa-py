from DS.binarytreenodes import BinaryTreeNode;
from DS.queues import Queue;

def minutesToBurnTree(root, firstburnnode):
    stack = [];
    q = Queue();
    burned = set();
    if root:
        stack.append((root, None));
        q.enqueue(firstburnnode);
        burned.add(firstburnnode);
    
    relationships = {  };
    while len(stack):
        child, parent = stack.pop();
        relationships[child] = parent;
        if child.right:
            stack.append((child.right, child));
        if child.left:
            stack.append((child.left, child));
    
    minutes = 0;
    while not q.empty():
        size = q.size();
        while size:
            node = q.dequeue();
            if node in relationships and relationships[node] and relationships[node] not in burned:
                q.enqueue(relationships[node]);
                burned.add(relationships[node]);
            if node.left and node.left not in burned:
                q.enqueue(node.left);
                burned.add(node.left);
            if node.right and node.right not in burned:
                q.enqueue(node.right);
                burned.add(node.right);
            size -= 1;

        if not q.empty():
            minutes += 1;

    return minutes;

root  = BinaryTreeNode(5);
root.left = BinaryTreeNode(2);
root.right = BinaryTreeNode(10);
root.left.left = BinaryTreeNode(45);
root.left.right = BinaryTreeNode(15);
root.right.right = BinaryTreeNode(16);
root.right.right.right = BinaryTreeNode(9);

# 9 ==> 5
print(minutesToBurnTree(root, root.right.right.right));
    
# 5 ==> 3
print(minutesToBurnTree(root, root));

# 45 ==> 5
print(minutesToBurnTree(root, root.left.left));

root2 = BinaryTreeNode(5);
root2.right = BinaryTreeNode(4);
root2.right.right = BinaryTreeNode(3);
root2.right.right.right = BinaryTreeNode(2);
root2.right.right.right.right = BinaryTreeNode(1);

# 5 ==> 4
print(minutesToBurnTree(root2, root2));

# 1 ==> 4
print(minutesToBurnTree(root2, root2.right.right.right.right));

# 3 ==> 2
print(minutesToBurnTree(root2, root2.right.right));