from DS.binarytreenodes import BinaryTreeNode;
from DS.queues import Queue;

def bottomSideView(root):
    q = Queue();
    seen = {  };
    if root:
        q.enqueue((root, 0));
    
    while not q.empty():
        node, offset = q.dequeue();
        seen[offset] = (node, offset);
        if node.left:
            q.enqueue((node.left, offset - 1));
        if node.right:
            q.enqueue((node.right, offset + 1));
    
    nodes = [value for key, value in seen.items()];
    nodes.sort(key=lambda x: x[1]);
    return [node[0].val for node in nodes];