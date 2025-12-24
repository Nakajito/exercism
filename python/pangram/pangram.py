def is_pangram(sentence):
    abecedary = 'abcdefghijklmnopqrstuvwxyz'
    sentence.lower()
    sentence = sentence.replace('_', ' ')
    
    print(sentence)
    
    if sentence == '':
        return False
    
    elif len(sentence) > 1:
        for letter in abecedary:
            if letter in sentence:
                return True
            else:
                return  False
                break