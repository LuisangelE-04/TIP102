'''
As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the most number of votes. If there is a tie, return any artist with the top number of votes.
'''

def best_set(votes):
  '''
  Understand: check for frequency of votes based of a dictionary with an integer as the key and the vote as the value.

  Iterating over each vote in votes wil give us the key, doing 
  for vote, artist in votes.items(): returns the key and artist result, we can use this to crate a frequency map,
  Therefore, frequency_map[artist] = 1 if it does not exist and frequency_map[artist] += 1 if it already exists
  Now we need to determine the highest value in the frequency_map. 
  '''

  '''
  frequency_map = {}

  for vote, artist, in votes.items():
    if artist in frequency_map:
      frequency_map[artist] += 1
    else:
      frequency_map[artist] = 1


  return max(frequency_map, key=frequency_map.get)
  '''
  frequency_map = {}
  for key, artist in votes.items():
    frequency_map[artist] = frequency_map.get(artist, 0) + 1

  return max(frequency_map, key=frequency_map.get)



votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
