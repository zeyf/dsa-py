from DS.binarytreenodes import BinaryTreeNode;
from DS.queues import Queue;

def topSideView(root):
    q = Queue();
    seen = set();
    if root:
        q.enqueue((root, 0));

    topnodes = [];
    while not q.empty():
        node, offset = q.dequeue();
        if offset not in seen:
            seen.add(offset);
            topnodes.append((node, offset));
        if node.left:
            q.enqueue((node.left, offset - 1));
        if node.right:
            q.enqueue((node.right, offset + 1));

    topnodes.sort(key=lambda x: x[1]);
    return [node[0].val for node in topnodes];