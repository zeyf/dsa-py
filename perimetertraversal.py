from DS.binarytreenodes import BinaryTreeNode;
from DS.queues import Queue;

def perimeterTraversal(root):
    q = Queue();
    if root:
        q.enqueue((root, 0));
    seen = set();
    seenOffsets = {  };
    leftview = [];
    exclusivebottomview = [];
    rightview = [];

    while not q.empty():
        size = q.size();
        leftmostlevelnode, leftmostleveloffset = q.front();
        rightmostlevelnode, rightmostleveloffset = q.tail();
        if leftmostlevelnode is not rightmostlevelnode: # more than one node on the level
            leftview.append(leftmostlevelnode.val);
            rightview.append(rightmostlevelnode.val);
            seen.add(leftmostlevelnode);
            seen.add(rightmostlevelnode);
        else: # only one node on level! must check if offset <= 0 or > 0 to see if it belongs to the left view or right view
            if leftmostleveloffset <= 0:
                leftview.append(leftmostlevelnode.val);
                seen.add(leftmostlevelnode);
            else:
                rightview.append(leftmostlevelnode.val);
                seen.add(leftmostlevelnode);
        while size:
            node, offset = q.dequeue();
            if node not in seen:
                seen.add(node);
                if offset not in seenOffsets:
                    seenOffsets[offset] = [(node, offset)];
                else:
                    seenOffsets[offset].append((node, offset));

            if node.left:
                q.enqueue((node.left, offset - 1));
            if node.right:
                q.enqueue((node.right, offset + 1));
            size -= 1;

    exclusivebottomview = [value for key, value in seenOffsets.items()];
    cleanbottomview = [];
    # still o(n). each array in the array is bounded to a size of 2 since in a binary tree the maximum node count overlap is 2 at any given coordinate.
    for nodes in exclusivebottomview:
        for node in nodes:
            cleanbottomview.append(node[0].val);

    return leftview + cleanbottomview + rightview[::-1];

