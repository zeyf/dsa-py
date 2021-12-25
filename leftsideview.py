from DS.binarytreenodes import BinaryTreeNode;
from DS.queues import Queue;

def leftSideView(root):
    q = Queue();
    if root:
        q.enqueue(root);
    view = [];

    while not q.empty():
        size = q.size();
        view.append(q.front().val);
        while size:
            node = q.dequeue();
            if node.left:
                q.enqueue(node.left);
            if node.right:
                q.enqueue(node.right);
            size -= 1;
    return view;