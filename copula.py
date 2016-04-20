import nltk

def copula(user_in):
  copula = 0
  copula_null = 0

  sentence = user_in
  tokens = nltk.word_tokenize(sentence)
  tagged = nltk.pos_tag(tokens)

  for i,tup in enumerate(tagged):
    word = tup[0]
    pos = tup[1]
    if (pos == 'PRP'):
      print "Pronoun"
      if tagged[i+1]:    
        next = tagged[i+1]
        next_word = next[0]
        next_pos = next[1]
        if (next_pos == 'VBZ'):
          copula = copula + 1
        else:
          copula_null = copula_null + 1
  print tagged
  print "Copula presence: " + str(copula) + " | Copula absence: " + str(copula_null)

def main():
  cont = True

  while (cont):
    user_in = raw_input("Enter sentence: ")
    copula(user_in)

    ask = raw_input("Continue? (Y/N) ")
    if (ask.upper() == "N"):
      cont = False
    else: continue

  print "Done!"

main()
