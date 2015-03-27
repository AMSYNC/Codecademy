def reverse(text):
    result = ""
    lenght = len(text)
    n = 1
    while n <= lenght:
        result += text[-n]
        n += 1
    print result
    return result
    

