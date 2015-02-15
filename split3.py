#The split() method can be called with no arguments.
#In this case, split() uses spaces as the delimiter. 
#Please notice that one or more spaces are treated the same.
#This split form handles sequences of whitespace.

#Program that uses split, no arguments: Python

# Input string.
# ... Irregular number of spaces between words.

s = "One two       three"

# Call split with no arguments.
words = s.split()

# Display results.
for word in words:
    print(word)