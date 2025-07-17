def find_treasure(matrix, treaure):
  rows = len(matrix)
  cols = len(matrix[0])
  
  for row in range(rows):
    for col in range(cols):
      if matrix[row][col] == treaure:
        return (row, col)
      
  return (-1, -1)



rooms = [
  [1, 4, 7, 11],
  [8, 9, 10, 20],
  [11, 12, 17, 30],
  [18, 21, 23, 40]
]

print(find_treasure(rooms, 17))
print(find_treasure(rooms, 5))