def my_function():
    print "Hello you! Let's play a game of Pig Latin!"
    complete = 0
    while complete != 1:
        word = raw_input("Enter an English word: ")
        if word.isalpha() == True:
            word = word + word[0]
            word_final = word[1:]
            print(word_final)
            complete = 1
        else:
            print("That is not a valid word!")
my_function()