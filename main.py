'''
Task 1: Reverse a String
(HINT: Review the Algorithms + Problem Solving Lecture!)
Write code that takes a string as input and returns the string reversed
i.e. “Hello” will be returned as “olleH”
'''

# start at the last letter (the length of the word - 1 will be the index of the final letter),
# then stop at -1 (because that would be the final letter of the word again) and step through it
# going backwards one at a time

word = "hello"
for i in range(len(word) -1, -1, -1): 
    print(word[i])                    

#tried using enumerate first and learned through a lot of frustrating debugging and googling that
#that will not work

'''
Task 2: Capitalize a Letter
Write code that takes a string as input and capitalize the first letter of each word. 
Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”
'''

# capitalized letters will appear either at the very first index (0) of a string or immediately
# after a space (if string[i-1] == " ") 

# string = "hello world"
# print(string.capitalize())

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

def is_palindrome_alternate(word):
    word_reversed = ''

    for i in range(len(word) -1, -1, -1): 
        word_reversed += word[i]

    if word_reversed == word:
        print("Yes")
    else:
        print("No")

is_palindrome_alternate("hello")

'''
Bonus Challenge
Task 4 : Compress a string of characters
For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"
'''

# def compress_string(string):

    # char_count = 0

    # for char in string:
    #     if 

