def remove_duplicates(sequence):
    newseq = []
    for n in sequence:
        if newseq.count(n) == 0:
            newseq.append(n)
    return newseq
    