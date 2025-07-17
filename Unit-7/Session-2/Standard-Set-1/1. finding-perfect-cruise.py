def find_cruise_length(cruise_lengths, vacation_length):
  def binary_search(array, target, left, right):
    if left > right:
      return False
    
    mid = (left + right) // 2

    if array[mid] == target:
      return True
    
    if array[mid] > target:
      return binary_search(array, target, left, mid - 1)
    else:
      return binary_search(array, target, mid + 1, right)

  return binary_search(cruise_lengths, vacation_length, 0, len(cruise_lengths) - 1)



print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))