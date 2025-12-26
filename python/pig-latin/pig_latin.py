def translate(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    # Frase handling
    if " " in text:
        words = text.split(" ")
        translated_words = [translate(word) for word in words]
        return " ".join(translated_words)

    # Rule 1 for words that start with a vowel sound
    if text.startswith(
        ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U", "yt", "xr", "Yt", "Xr")
    ):
        return text + "ay"

    # Rule 3 for "qu" at the start of a word
    if text[0] == "q" and text[1] == "u":
        return text[2:] + "quay"

    elif (text[0] in consonants) and (text[1] == "q" and text[2] == "u"):
        return text[3:] + text[0] + "quay"

    # Rule 4 for consonant followed by 'y'
    if text[0] in consonants and (text[1] == "y"):
        return text[1:] + text[0] + "ay"
    elif (text[0] in consonants and text[1] in consonants) and (text[2] == "y"):
        return text[2:] + text[0:2] + "ay"

    # Rule 2 for consonant clusters
    if (text[0] in consonants) and (text[1] in consonants) and (text[2] in consonants):
        return text[3:] + text[0:3] + "ay"

    elif (text[0] in consonants) and (text[1] in consonants):
        return text[2:] + text[0:2] + "ay"

    elif text[0] in consonants:
        return text[1:] + text[0] + "ay"


print(translate("school"))
