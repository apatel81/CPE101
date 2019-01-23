#Lab 6
#Name: Ajay Patel
#Section 1

def is_lower_101(character):
    #Take a character, check the value, and return true if it is in the range of lowercase letters
    #str ----> True/Fale
    if ord(character) >= ord('a') and ord(character) <= ord('z'):
       return True
    else:
       return False

def char_rot13(character):
    #Take a character, add 13 to it, and return new letter
    #str ---> str
    letter = ord(character)
    if letter >= ord('A') and letter <= ord('M'):
       newletter = letter + 13
    elif letter >= ord('N') and letter <= ord('Z'):
       newletter = letter -13
    elif letter >= ord('a') and letter <= ord('m'):
       newletter = letter + 13
    elif letter >= ord('n') and letter <= ord('z'):
       newletter = letter - 13
    else:
       return False
 
    return chr(newletter)
    
