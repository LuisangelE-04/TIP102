'''
Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in the lst. Do not use any built-in functions.
'''

def linear_search(lst, target):
  for i in range(len(lst)):
    if lst[i] == target:
      print(i)
      return

  print(-1)
  return

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)
