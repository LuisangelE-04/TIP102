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


def find_flower(inventory, name):
  ''''
  :rtype: bool
  '''
  if not inventory:
    return False
  
  if inventory.val == name:
    return True
  
  left = find_flower(inventory.left, name)
  right = find_flower(inventory.right, name)
  
  return left or right


"""
          Rose
         /    \
      Lilac  Tulip
      /  \       \
   Daisy Lily   Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower"))