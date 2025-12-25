def is_pangram(sentence):
    abecedary = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    sentence = sentence.replace("_", " ")

    if sentence == "":
        return False

    elif len(sentence) > 1:
        for letter in abecedary:
            if letter not in sentence:
                return False
        return True
    else:
        return False
