""" """

import time
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val or p.left != q.left or p.left != q.left:
            return False
        return True


if __name__ == "__main__":
    start_time = time.time()
    Tree1 = TreeNode(1, 2, 3)
    Tree2 = TreeNode(1, 2, 3)
    print(Solution().isSameTree(Tree1, Tree2))

    Tree1 = TreeNode(1, None, 3)
    Tree2 = TreeNode(1, 2, 3)
    print(Solution().isSameTree(Tree1, Tree2))

    print("--- %s seconds ---" % (time.time() - start_time))
