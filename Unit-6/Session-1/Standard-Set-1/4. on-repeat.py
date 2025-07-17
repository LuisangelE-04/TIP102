class SongNode:
  def __init__(self, song, artist, next=None):
    self.song = song
    self.artist = artist
    self.next = next

def on_repeat(playlist_head):
  slow = playlist_head
  fast = playlist_head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
      return True
  
  return False

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))

# return true