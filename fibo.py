def fibo(number,limit=50,filename="fibonnaci.txt"):
    with open(filename, "w") as my_file:
        a1 = 0
        a2 = 1
        if type(number) != int or number < 1:
            my_file.write("This is not a valid Fibonacci sequence!"+"\n")
        elif type(limit) != int or limit < 1:
            my_file.write("This is not a valid limit!"+"\n")
        elif limit > 1000:
            my_file.write("This limit is too high!"+"\n")
        else:
            my_file.write(("Calculating Fibonacci Sequence up to step {0} and to output limit {1}").format(number, limit)+"\n")
            my_file.write("Step 1: seeding numbers 0 and 1..."+"\n")
            count = 2
            n = a1 + a2
            my_file.write(("Step {0}: {1}+{2}={3}").format(count, a1, a2, n)+"\n") 
            while count < number:
                if count < limit:
                    a1 = a2
                    a2 = n
                    n = a1 + a2
                    count += 1
                    my_file.write(("Step {0}: {1}+{2}={3}").format(count, a1, a2, n)+"\n")
                else:
                    my_file.write(("limit of {0} reached! Ending Fibonacci calculation.").format(limit)+"\n")
                    return n
                    break
            return n