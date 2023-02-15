'''
Task 1: Reverse a String
(HINT: Review the Algorithms + Problem Solving Lecture!)
Write code that takes a string as input and returns the string reversed
i.e. “Hello” will be returned as “olleH”
'''
# start at the last letter (the length of the word - 1 will be the index of the final letter),
# then stop at -1 (because stop is not inclusive so if we want index[0] to be included, 
# we have to set our stopping point to one element beyond that) and step through it
# going backwards one at a time

def reverse_string(string):
    new_string = ''
    for i in range(len(string) -1, -1, -1): 
        new_string += string[i] 
    return(new_string)    

# tried using enumerate first and learned through a lot of frustrating debugging and googling that
# that will not work

# reverse_string("hello")      

def reverse_string_alternate(string):
    new_string = ''
    for i in string:
        string[i] += new_string
    return new_string

print(reverse_string_alternate("hello"))

'''
Task 2: Capitalize a Letter
Write code that takes a string as input and capitalize the first letter of each word. 
Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”
'''
# capitalized letters will appear either at the very first index (0) of a string or immediately
# after a space (if string[i-1] == " ") 

# string = "hello world"
# print(string.title())

def cap_first_letter(string):
    new_string = ''
    
    for i in range(len(string)):
        if i == 0:
            # print(string[i].upper())
            new_string += string[i].upper()
        elif string[i -1] == " ":
            # print(string[i].upper())
            new_string += string[i].upper()
        else:
            print(string[i])
            # new_string += word[i]
            new_string += string[i]

    print(new_string)

cap_first_letter("hello world")

'''
Task 3: Palindrome
A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	
Write code that takes a user input and checks to see if it is a Palindrome and reports the result
'''

# try to adjust for palindromes that include spaces or punctuation
# a man, a plan, a canal: PANAMA

def is_palindrome(word):
    word = input("What word would you like to check? > ").lower()
    word_reversed = reverse_string(word)

    # for i in range(len(word) -1, -1, -1): 
    #     word_reversed += word[i]

    if word_reversed == word:
        print("Yes")
    else:
        print("No")

is_palindrome()

def is_palindrome_alternate(word):

# walking through one letter at a time, forwards and backwards
# forwards will start with index 0 and go up to the len(word) - 1
# backwards will start with index -1 and will go down to -len(word)

    word = input("What word would you like to check? > ").lower()
    reverse_string = ''

    for i in range(len(word)):
        # print(word[i])
        # print(word[-1 - i])
# 0, 1, 2, 3
#-1,-2,-3,-4 
        if word[i] != word[-1 - i]:
            print("That is not a palindrome.")
            return 
    # if nothing causes the above to happen and break the loop (return), then we know that 
    # our input is a palindrome, so we don't need an elif/else/etc
    print("Yes, that is a palindrome.")

# halfway = int(len(word)/2) # can add +1 if you want it to explicitly check the middle character
# for i in range(halfway):
# ^ works bc if there are an odd number of characters, the middle character doesn't matter
# it just needs the letters outside of it to mirror one another 

'''
Bonus Challenge
Task 4 : Compress a string of characters
For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"
'''
# for each instance of a character, output should be the number of times that character appears
# and then the character referenced by the number 

def compress_string(string):
    pass

# if character after character you are looking at is the same as the character you're currently
# looking at, then add to count for that character and then check if the next one is also the same, 
# once the next character is different, add your count and your character to a new string, continue
# through string until length of original string has been covered
        

