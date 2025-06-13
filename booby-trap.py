'''
To disable the trap, Captain Feathersword must remove exactly one letter from the message.
'''

def is_balanced(code):
  original_frequences = {}
  for char in code:
    original_frequences[char] = original_frequences.get(char, 0) + 1

  for char_to_remove in original_frequences:
    curruent_counts = original_frequences.copy()

    curruent_counts[char_to_remove] -= 1

    active_frequencies = []

    for count in curruent_counts.values():
      if count > 0:
        active_frequencies.append(count)

    if not active_frequencies:
      return True
    
    if len(set(active_frequencies)) <= 1:
      return True
    
  return False

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 