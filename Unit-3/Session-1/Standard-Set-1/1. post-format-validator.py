'''
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.
'''

def is_valid_post_format(posts):
  stack = []
  keys = {'(' : ')', '[' : ']', '{' : '}'}

  for char in posts:
    if char in keys:
      stack.append(char)
    elif char in keys.values():
      if not stack or keys[stack[-1]] != char:
        return False
      
      stack.pop()
  
  return len(stack) == 0

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))