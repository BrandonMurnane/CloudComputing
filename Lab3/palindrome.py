string1="Oxo"
string2="OXO"
string3="12345321"
string4="ROTATOR"
string5="12345 54321"


def del_space(word):
    word = word.replace(" ","")
    word = word.lower()
    print(word)
    return word
  
def rev_word(word):
    reversed_word = word[::-1]
    print(reversed_word)
    return reversed_word
  
del_space(string1)
rev_word(string1)
del_space(string2)
rev_word(string2)
del_space(string3)
rev_word(string3)
del_space(string4)
rev_word(string4)
del_space(string5)
rev_word(string5)
