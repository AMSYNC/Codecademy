def purify(numbers):
    newlist = []
    removed = []
    for x in numbers:
        if x % 2 == 0:
            newlist += x
    return newlist