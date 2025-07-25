from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
    self.key = key
    self.val = value
    self.left = left
    self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
    if isinstance(item, tuple):
      return item[0], item[1]
    else:
      return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
    node = queue.popleft()
    if index < len(values) and values[index] is not None:
      left_key, left_value = get_key_value(values[index])
      node.left = TreeNode(left_value, left_key)
      queue.append(node.left)
    index += 1
    if index < len(values) and values[index] is not None:
      right_key, right_value = get_key_value(values[index])
      node.right = TreeNode(right_value, right_key)
      queue.append(node.right)
    index += 1

  return root

from collections import deque 

def print_tree(root):
  if not root:
    return "Empty"
  result = []
  queue = deque([root])
  while queue:
    node = queue.popleft()
    if node:
      result.append(node.val)
      queue.append(node.left)
      queue.append(node.right)
    else:
      result.append(None)
  while result and result[-1] is None:
    result.pop()
  print(result)


def count_odd_splits(root):
  '''
  :rtype: int

  traverse entire tree
  check if value for each node is odd
  if odd, add 1 to count
  if even, add 0 to count
  '''

  if not root:
    return 0
  
  left = count_odd_splits(root.left)
  right = count_odd_splits(root.right)

  if root.val % 2 == 1:
    return left + right + 1
  else:
    return left + right


"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))
