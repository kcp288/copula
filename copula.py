import nltk

copula_list = []
sentences = []

def get_pos(token):
  word = token[0]
  pos = token[1]
  return word, pos

def print_copula(copula_list):
  total = len(copula_list)

  if (total < 1): return

  present = 0
  absent = 0

  for i in copula_list:
    if (i[0] == 0):
      present = present + 1
    elif (i[0] == 1):
      absent = absent + 1
    else:
      continue

  present_per = float(present)/total * 100
  absent_per = float(absent)/total * 100

  print '\nTotal copula spaces:\t' + str(total) + '\n' + \
  'Present:\t' + str(present) + '/' + str(total) + '\t (' + "{0:.2f}".format(present_per) + '% of total)\n' + \
  'Absent:\t' + str(absent) + '/' + str(total) + '\t (' + "{0:.2f}".format(absent_per) + '% of total)\n'

def copula(user_in):
  
  

  # 0: 0 - present, 1 - absent
  # 1: 0 - 'is', 1 - 'are'
  # 2: 0 - after 'PRP', 1 - after NOUN
  # 3: 0 - before 'JJ', 1 - before NOUN, 2 - before GONNA


  # COPULA DELETION FEATURES
  # IS | ARE 
  # AFTER PRONOUN | NOUN
  # BEFORE ADJECTIVE | NOUN | GONNA/GON/GOING TO 

  sentence = user_in.upper()
  tokens = nltk.word_tokenize(sentence)
  tagged = nltk.pos_tag(tokens)

  for i,tup in enumerate(tagged):
    try:
      copula = [0,0,0,0]
    
      word, pos = get_pos(tup)

      # Eliminate cases
        # If before '.' (not sentence final)
        # Not contracted 's
        # Not first person "am"
        # Not infinitive 'be'
        # Not ain't
      
      if (pos == 'PRP') or (pos == "NN") or (pos == "NNS") or (pos == "NNP"):
        # Not sentence final
        # TODO: Check period
        try:
          next = tagged[i+1]
          next_word = next[0]
          if next_word == 'AM': 
            print "First person"
            break
        except IndexError:
          pass
    

      # Following a PRONOUN
      if (pos == 'PRP'):
        # Make su
        if tagged[i+1]:    
          next_word, next_pos = get_pos(tagged[i+1])
          fol_word, fol_pos = get_pos(tagged[i+2])
          if (next_word == 'IS') or (next_word == 'ARE'):
            copula[0] = 0

          else:
            copula[0] = 1

        copula_list.append(copula)
        print_copula(copula_list)

      
      # Following a NOUN (less likely) 
      if (pos == "NN") or (pos == "NNS") or (pos == "NNP"):
        if tagged[i+1]:    
          next_word, next_pos = get_pos(tagged[i+1])
          fol_word, fol_pos = get_pos(tagged[i+2])
          if (next_word == 'IS') or (next_word == 'ARE'):
            copula[0] = 0
          else:
            copula[0] = 1
        copula_list.append(copula)
        print_copula(copula_list)

      
    except IndexError:
      pass
  # print tagged
  # print "Copula presence: " + str(copula) + " | Copula absence: " + str(copula_null)
  sentences.append(tagged)
  pretty_print(sentences)

  #print_copula(copula_list)

def pretty_print(arr):
  for i in arr:
    print i
  print ''

def main():
  cont = True

  while (cont):
    user_in = raw_input("Enter sentence: ")
    copula(user_in)

    ask = raw_input("Continue? (Y/N) ")
    if (ask.upper() == "N"):
      cont = False
    else:
      clear = raw_input("Clear? (Y/N) ")
      if (clear.upper() == "Y"):

        copula_list = []
        sentences = []
        print copula_list, sentences
      else: continue

  print "Done!"

main()
