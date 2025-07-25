'''
You're planning an epic trip and have a dictionary of destinations mapped to their respective rating scores. Your goal is to visit only the best-rated destinations. Write a function that takes in a dictionary destinations and a rating_threshold as parameters. The function should iterate through the dictionary and remove all destinations that have a rating strictly below the rating_threshold. Return the updated dictionary.
'''

def remove_low_rated_destinations(destinations, rating_threshold):
  '''
  new_dict = {}
  for key, rating in destinations.items():
    if rating >= rating_threshold:
      new_dict[key] = rating

  return new_dict
  '''
  keys_to_remove = []
  for key, rating in destinations.items():
    if rating < rating_threshold:
      keys_to_remove.append(key)

  for key in keys_to_remove:
    del destinations[key]
  
  return destinations

destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

print(remove_low_rated_destinations(destinations, 4.0))
print(remove_low_rated_destinations(destinations2, 4.9))
