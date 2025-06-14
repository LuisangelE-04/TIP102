'''
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.
'''
def tiggerfy(word):
  to_remove = ["t", "i", "gg", "er"]

  

  for substring in to_remove:
    if substring in word:
      print(substring)

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
