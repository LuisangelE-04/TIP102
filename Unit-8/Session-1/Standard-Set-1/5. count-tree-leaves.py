class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def count_leaves(root):
  # count every node in the tree
  # for each node, check if left or right exists, if yes we return 1 else we return 0
  # if current_node.left or current_node.right
  # if yes, we continue, else we add to count

  def helper(node):
    if not node:
      return 0
    if not node.right and not node.left:
      return 1
    
    left_leaves = helper(node.left)
    right_leaves = helper(node.right)

    return left_leaves + right_leaves
  
  return helper(root)

  return leaf_nodes


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 =  TreeNode("Root", 
        TreeNode("Node1", TreeNode("Leaf1")),
        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))