'''
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.
'''

def is_symmetrical_title(title):
  new_title = ""
  for char in title:
    if char != " ":
      new_title += char.lower()

  ptr_1 = 0
  ptr_2 = len(new_title) - 1

  while ptr_1 < ptr_2:
    if new_title[ptr_1] != new_title[ptr_2]:
      return False
    ptr_2 -= 1
    ptr_1 += 1
    
  return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 