from collections import deque

class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

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


def max_tiers(cake):
  if not cake:
    return 0

  left = max_tiers(cake.left)
  right = max_tiers(cake.right)

  return 1 + max(left, right)



"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))

