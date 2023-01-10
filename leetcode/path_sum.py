class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)


def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node
    return inner()


tree = to_binary_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])



def hasPathSum(root, targetSum, sum, node_stack = [], sum_stack = []):
    if not root:
        return False
    sum = sum + root.val

    if not root.left and not root.right and sum == targetSum:
        return True
    if root.left:
        node_stack.append(root)
        sum_stack. append(sum)
        if hasPathSum(root.left, targetSum, sum):
            return True
        if hasPathSum(root.right, targetSum, sum) == None:
            return False
    if root.right:
        if hasPathSum(root.right, targetSum, sum):
            return True
        if hasPathSum(root.right, targetSum, sum) == None:
            return False


    if not node_stack:
        prev_node = node_stack.pop()
        prev_sum = sum_stack.pop()
        if hasPathSum(prev_node.right, targetSum, prev_sum):
            return True
        else: 
            return False

    

    

print(hasPathSum(tree, 22, 0))

