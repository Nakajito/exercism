def translate(text):
    vowel ='aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'

    if (len(text) < 3):
        return text[1:] + text[0] + 'ay'
    
    elif (text[0] in consonant) and (text[1] == 'q') and (text[2] == 'u'):
        return text[3:] + text[0:3] + 'ay'
    
    elif (text[0] in consonant) and (text[1] in consonant) and (text[2] == 'y'):
        return text[2:] + text[0:2] + 'ay'
    
    elif (text[0] == 'q') and (text[1] == 'u'):
        return text[2:] + text[0:2] + 'ay'
    
    elif (text[0] in consonant) and (text[1] == 'y'):
        return text[1:] + text[0] + 'ay'
    
    elif (text[0] == 'x' and text[1] == 'r'):
        return text + 'ay'
    
    elif (text[0] == 'y' and text[1] == 't'):
        return text + 'ay'
    
    elif (text[0] in consonant) and (text[1] in consonant) and (text[2] in consonant):
        return text[3:] + text[0:3] + 'ay'
    
    elif (text[0] in consonant) and (text[1] in consonant):
        return text[2:] + text[0:2] + 'ay'
    
    elif (text [0] in consonant):
        return text[1:] + text[0] + 'ay'
    
    elif (text[0] in vowel):
        return text + 'ay' 
    
    else:
        return text + 'ay'

text = 'ick dast runquay'

print(translate(text))
