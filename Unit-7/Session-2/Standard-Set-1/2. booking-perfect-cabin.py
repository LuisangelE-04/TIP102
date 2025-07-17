def find_cabin_index(cabins, preferred_deck):
  left = 0
  right = len(cabins) - 1

  while left <= right:
    mid = (left + right) // 2

    if cabins[mid] == preferred_deck:
      return mid
    elif cabins[mid] > preferred_deck:
      right = mid - 1
    else:
      left = mid + 1

  return mid + 1

print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))