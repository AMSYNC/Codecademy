def anti_vowel(text):
    newtext = ""
    removed = ""
    for i in text:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" \
        or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            removed += i
        else:
            newtext += i
    print removed
    print newtext
    return newtext