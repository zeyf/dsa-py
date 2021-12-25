from DS.binarytreenodes import BinaryTreeNode;
from DS.queues import Queue;

def rightSideView(root):
    q = Queue();
    if root:
        q.enqueue(root);
    view = [];

    while not q.empty():
        size = q.size();
        view.append(q.front().val);
        while size:
            node = q.dequeue();
            if node.right:
                q.enqueue(node.right);
            if node.left:
                q.enqueue(node.left);
            size -= 1;
    return view;