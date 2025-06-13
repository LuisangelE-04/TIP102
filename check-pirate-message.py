def can_trust_message(message):
  characters = set()
  for character in message:
    characters.add(character)

  if len(characters) == 27:
    return True
  else:
    return False



message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))