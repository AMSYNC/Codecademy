def censor(text, word):
    # text = text.lower()
    # word = word.lower()
    replace = ""
    for x in word:
        replace += "*"
    textlst = text.split()
    for i,x in enumerate(textlst):
        if x == word:
            textlst[i] = replace
    newtext = ""
    for x in textlst:
        newtext += x + " "
    newtext = newtext[:-1]
    print newtext
    return newtext