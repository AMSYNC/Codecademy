def count(sequence, item):
    counter = 0
    emplist = []
    if type(item) == type(emplist):
        for n in item:
            counter += sequence.count(n)
        return counter
    else:
        for x in sequence:
            if x == item:
                counter += 1
        return counter  