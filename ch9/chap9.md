## Dictionaries ##

A **list** is a linear collection of values that stay in order, a **dictionary** is a collection of values each with its own key.  Also called Associate Arrays (Perl/PHP), Properities or Map or HashMap (Java).

e.g.
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])

e.g. (for, in)
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

e.g. (get method)
if name in counts:
    x = counts[name]
else :
    x = 0
x = counts.get(name, 0)

e.g. simplified
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
prints(counts)

e.g. Counting a pattern
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:' words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

e.g. counting keys
for key in counts:
    print(key, counts[key])