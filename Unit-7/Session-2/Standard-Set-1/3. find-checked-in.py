def count_checked_in_passengers(rooms):
  left = 0
  right = len(rooms) - 1
  length = len(rooms)

  while left <= right:
    mid = (left + right) // 2

    if rooms[mid] == 1:
      if rooms[mid - 1] == 1:
        right = mid - 1
      else:
        return length - mid
    elif rooms[mid] == 0:
      left = mid + 1

  return 0


rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))