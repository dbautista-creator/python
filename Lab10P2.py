# get user input

strng = input('Enter a string : ')

# create an array of size 26 as the number of capital letters are 26

# each i th index store the count of capital alphabet where

# index 0 store A

# index 1 store B

# .

# .

# .

# index 25 store Z

count = [0] * 26

# read strng character by character

# upper() function convert string into upper case

for ch in strng.upper():

    # calculate the ascii value of an element using

    # ord() function in python

    ascii = ord(ch)

    # if current character is a capital alphabet

    if ascii >= 65 and ascii <= 90:
        # calculate index in count list

        index = ascii - 65

        count[index] += 1

for i in range(0, len(count)):

    if count[i] > 0:
        print('%10s %10d' % (chr(i + 65), count[i]))