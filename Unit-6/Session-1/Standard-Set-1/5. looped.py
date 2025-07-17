class SongNode:
  def __init__(self, song, artist, next=None):
    self.song = song
    self.artist = artist
    self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
  slow = playlist_head
  fast = playlist_head

  cycle_size = 0
  count = 0

  # solution is incorrect for different test cases
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      count += 1

    if count == 1:
      cycle_size += 1
    elif count == 2:
      return cycle_size


song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song5 = SongNode("Gangam Style", "PSY")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song5
song5.next = song2

print(loop_length(song1))

# prints 3

