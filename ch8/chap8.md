## Lists ##

**Algorithms** A set of tules or steps used to solve a problem

**Data Structures** A particular way of organizing data in a computer

A **collection** allows us to put many values in a single variable

**List** constants are surrounded by squared brackets, can be any Python element, can be empty

Strings are **immutable**, lists are **mutable**

The **range** function returns a list of numbers from zero to one less than the parameter (e.g. to create a **counted loop**)

Lists can be **concatenanted** and **sliced** just like strings, and can be modified using methods (e.g. **append**, **in**, **not in**, **len**, **max**, **min**)

Lists will maintain order, so output will be in the same order as input unless using **sort** method

e.g. (calculating average using list methods)
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

The **split** method breaks a string into parts and produces a list of strings

e.g. (double split pattern from prior email address example)
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])