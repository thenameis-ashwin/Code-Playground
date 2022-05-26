a = "ashwin"
print(a.capitalize())  # returns the string with first letter capital
print(a.upper())  # returns everything in uppercase
print(a.lower())  # returns everything in lowercase
c = "retro geeks owned by retro geeks"
print(c.title())  # returns everything with first letter of every word capital
print(c.count('geeks', 10, 32))  # counts the no.of times a particular string occurs in String
print(len(c))  # finds the length of a string
print(c.find('retro', 10, 32))  # find the occurance of a particular string
print(c.replace('retro', 'abcd'))  # to replace a particular string
print(c.swapcase())  # to swap the case of characters in a particular string

myTuple = ("Retro Geeks", "owned by", "Ashwin")  # Multiple strings
x = " ".join(myTuple)  # uses join function to join these words in a tuple using a seperator
print(x)
