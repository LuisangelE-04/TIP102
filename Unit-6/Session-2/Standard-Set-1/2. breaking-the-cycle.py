class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def collect_false_evidence(evidence):
	# 1st loop checks if a cycle exists and length of cycle
  # 2nd loop returns the values in the cycle
  # if cycle exists, return array/list of values
  # if a cycle does not exists, return empty array/list

  current = evidence
  slow = evidence
  fast = evidence
  count = 0
  false_clues = []

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      break
    else:
      return false_clues
    
  start = evidence

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))