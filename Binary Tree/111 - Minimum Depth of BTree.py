

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
        O(n)
    '''

    # DFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # BFS
    def minDepth2(self, root):
        if not root:
            return 0
        queue, depth = deque([root]), 1
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                elif not (node.left or node.right):
                    return depth
                else:
                    queue.append(node.left)
                    queue.append(node.right)
            depth += 1
        return depth


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)
ob = Solution()
print(ob.minDepth(root))
print(ob.minDepth2(root))
