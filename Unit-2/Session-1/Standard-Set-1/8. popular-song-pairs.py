'''
Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist, return the number of popular song pairs.

A pair (i, j) is called popular if the songs have the same popularity score and i < j.

Hint: number of pairs = (n x n-1)/2
'''

def num_popular_pairs(popularity_scores):
  '''
  Understand: Count pairs of songs that have the same popularity score, where the first song comes before the second song in the array.

  Key Concepts
  Pair (i, j): Two positions in the array where i < j (first index is smaller than second)
  Popular pair: Both songs at positions i and j have the same popularity score
  Count all such pairs
  Example Walkthrough
  Step 1: Find all possible pairs where i < j

  (0,1), (0,2), (0,3), (0,4), (0,5)
  (1,2), (1,3), (1,4), (1,5)
  (2,3), (2,4), (2,5)
  (3,4), (3,5)
  (4,5)
  Step 2: Check which pairs have same popularity scores

  (0,3): scores[0]=1, scores[3]=1 ✅ Popular pair
  (0,4): scores[0]=1, scores[4]=1 ✅ Popular pair
  (2,5): scores[2]=3, scores[5]=3 ✅ Popular pair
  (3,4): scores[3]=1, scores[4]=1 ✅ Popular pair
  
  Result: 4 popular pairs
  '''
  frequency_map = {}

  for score in popularity_scores:
    frequency_map[score] = frequency_map.get(score, 0) + 1

  print(frequency_map)
  
  total_pairs = 0
  for count in frequency_map.values():
    if count > 1:
      total_pairs += count * (count - 1) // 2

  return total_pairs

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3))