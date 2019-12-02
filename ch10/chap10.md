## Tuples ##

Like lists, but using parentheses to define.  Unlike a list, **Tuples are immutable**. (allows them to be stored more denseley than lists)

Can put a Tuple on the LHS of an assignment statement:
(x, y) = (4, 'fred')
print(y)

The **items()** method in dictionarieis returns a list of (key, value) tuples:
for (k,v) in d.items():
    print(k, v)

The **comparison** operations work with tuples and other sequences.

We can use tuples to get a sorted version of a dictionary by key using **items()** and **sorted()** functions.

If we construct a list of tuples of the form **(value, key)**, we could sort by value in stead of key.

**List Comprehension** creates a dynamic list.  This would help to make a list of reversed tuples and then sort it:
c = {'a':10, 'b':1, 'c':22}
print( sorted( { (v,k) for k,v in c.items() } ) )