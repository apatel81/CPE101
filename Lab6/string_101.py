#Lab 6
#Name: Ajay Patel
#Section 1

def str_rot_13(word):
    #Rotate each character in a word 13 letters
    #str ---> str
    result = ''
    for letter in word:
       letter = ord(letter)
       if letter >= ord('A') and letter <= ord('M'):
          newletter = letter + 13
       elif letter >= ord('N') and letter <= ord('Z'):
          newletter = letter - 13 
       elif letter >= ord('a') and letter <= ord('m'):
          newletter = letter + 13
       elif letter >= ord('n') and letter <= ord('z'):
          newletter = letter - 13
       else:
          return False
    
       result += chr(newletter)
   
    return result


def str_translate_101(word, letter, newletter):
    #Replace the letters of a word with a new letter
    #str ---> str
    s = (word)
    w = s.replace(letter, newletter)
    return w
