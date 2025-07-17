def count_suits_iterative(suits):
  suit_set = set(suits)
  count = 0

  for suit in suit_set:
    count += 1

  return count

def count_suits_recursive(suits):
  unique_list = []
  return helper(unique_list, suits)

def helper(unique_list, suits):
  if not suits:
    return 0
  
  if suits[0] not in unique_list:
    unique_list.append(suits[0])
    return 1 + helper(unique_list, suits[1:])
  
  return helper(unique_list, suits[1:])

print(count_suits_iterative(["Mark I", "Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark III", "Mark IV"]))