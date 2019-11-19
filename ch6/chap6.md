A **string** is a sequence of characters.

e.g.
fruit = 'banana'
letter = fruit[1]
print(letter)
>>>a
x = 3
w = fruit[x -1]
print(w)
>>>n

Get a **python error** if attempt to index beyond the end of a string.

Length function: len(fruit)

e.g. Indeterminate loop to go through all letters using a **while** loop
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

or... Definite loop using a **for** statement (much more elegant)
fruit = 'banana'
for letter in fruit:
    print(letter)

Can also look at continious section of a string using a **colon operator** to slice
e.g.
s = 'Monty Python'
print(s[0:4])
>>>Mont
print(s[6:7])
>>>P
print(s[:2])
>>>Mo
print(s[8:])
>>>thon
print(s[:])
>>>Monty Python

## Manipulating Strings ##

* Use the '+' operator for string concatenation
* USe the 'in' keyword to check to see if one string is in another
* Use > or < for comparisons -- upper case sorts before lower case

Python has a number of functions in the **string library**, e.g. 'lower' -- these do not modify the original string, instead they return a new string that has been altered (see online documentation)

* Use the 'find()' function to locate something in the string
* Use the 'replace()' function to search and replace all occurrences
* Use 'lstrip()' 'rstrip()' or strip() to remove whitespace
