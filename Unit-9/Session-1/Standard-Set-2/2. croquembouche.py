from collections import deque

class Puff():
  def __init__(self, flavor, left=None, right=None):
    self.val = flavor
    self.left = left
    self.right = right

def print_design(design):
  # use a queue to add tree nodes in level order traversal
  # root, left, right
  # :rtype: list []

  if not design:
    return []
  
  queue = deque([design])
  list = []


  while queue:
    current = queue.popleft()
    list.append(current.val)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  print(list)



"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                Puff("Strawberry"))
print_design(croquembouche)