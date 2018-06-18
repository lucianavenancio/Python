"""#Gettin characters from the position 1
a = "hello"
print(a[1])

#Gettin characters from the position 2
b = "world"
print(b[2:5])

#The strip() method removes any whitespace from the beginning or the end
c = " Hello, World! "
print(c.strip()) #returns Hello World

#The len() method returns the length of a string
d = "Hello World"
print(len(d))

#The lower() method returns the string in lower case
e = "Hello World"
print(e.lower())

#The upper() method returns the string in upper case
f = "Hello World"
print(f.upper())

#The replace() method replaces a string with another string
g = "Hello World"
print(g.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator
h = "Hello World"
print(h.split(","))"""

#COMMAND-LINE STRING INPUT
print("Enter your name:")
x = input()
print("Hello, " + x)