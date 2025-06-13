'''
You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.

Return the combined audience size of all performances in audiences with the maximum audience size.

The audience size of a performance is the number of people who attended that performance.
'''

def max_audience_performances(audiences):
  '''
  Understand: Return max audience size in list. If multiple max add and combine. 
  Retrieve max by getting each index into a dictionary with the value of the audience using enumerate.
  for index, audience in enumerate(audience): my_dict[index] = audience
  '''
  '''
  return sum(audience for audience in audiences if audience == max(audiences))
  '''
  frequency_map = {}

  for audience in audiences:
    frequency_map[audience] = frequency_map.get(audience, 0) + 1

  max_audience = max(frequency_map.keys())

  return max_audience * frequency_map[max_audience]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
