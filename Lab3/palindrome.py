strings=["Oxo","OXO","12345321","ROTATOR","12345 54321"]

def del_space(word):
    word = word.replace(" ","")
    word = word.lower()
    print(word)
    return word

def rev_word(word):
    reversed_word = word[::-1]
    print(reversed_word)
    return reversed_word


for word in strings:
  if(rev_word(word) == del_space(word)):
      print(reversed_word + " AND " + del_space)
      print("Palindrome")
      break;
  else:
      print("Not a palindrome")



