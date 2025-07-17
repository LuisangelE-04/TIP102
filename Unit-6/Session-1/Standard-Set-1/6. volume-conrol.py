class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
  current = head
  while current:
    print(current.value, end=" -> " if current.next else "\n")
    current = current.next

def count_critical_points(song_audio):
  current = song_audio.next
  prev = song_audio
  count = 0

  while current.next:
    if current.value > prev.value and current.value > current.next.value:
      count += 1
    
    if current.value < prev.value and current.value < current.next.value:
      count += 1
    
    prev = current
    current = current.next

  return count


song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))