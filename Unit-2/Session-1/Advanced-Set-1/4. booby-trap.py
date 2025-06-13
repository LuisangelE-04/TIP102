'''
Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a function is_balanced() that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.
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