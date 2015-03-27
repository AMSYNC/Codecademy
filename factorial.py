
def factorial(x):
    if x > 0:
        y = ""
        while x != 0:
            x = str(x)
            y += "%s*" % (x)
            x = int(x)
            x -= 1
        result = y[:-1]
        print eval(result)
        return eval(result)
    else:
        print "cannot do negative or 0 factorials!"
        
