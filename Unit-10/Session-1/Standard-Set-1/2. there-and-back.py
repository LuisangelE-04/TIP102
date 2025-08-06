def bidirectional_flights(flights):
  '''
  4 different flights
  want to check if each flight is bidirectional
  2 for loops with variables i and j
  '''

  for i in range(len(flights)):
    for j in flights[i]:
      if i not in flights[j]:
        return False
      else:
        continue
  
  return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))