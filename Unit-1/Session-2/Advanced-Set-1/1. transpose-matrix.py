def transpose(matrix):
  new_matrix = []

  for i in range(len(matrix[0])):
    for j in range(len(matrix)):
      new_matrix[j][i] = matrix[i][j]

  print(new_matrix)

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
transpose(matrix)

matrix = [
  [1, 2, 3],
  [4, 5, 6]
]
transpose(matrix)