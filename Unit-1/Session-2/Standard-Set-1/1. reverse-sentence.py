def reverse_sentence(sentence):
  words = sentence.split()
  sentence_size = len(words)

  if sentence_size == 1:
    print(sentence)
  else:
    words = reversed(words)
    sentence = ' '.join(words)
    print(sentence)

  


sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)