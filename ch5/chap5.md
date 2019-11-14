## Loops and Iteration ##

Loops have **iteration variables** that change each time through a loop.  Often these **iteration variables** go through a sequence of numbers.

e.g.
    n = 5
    while n > 0 :
        print(n)
        n = n-1
    print('Blastoff')
    print(n)

The **break** statement ends the current loop and jumps to the statemenet immediately following the loop.

e.g.
    while True:
        line = input('> ')
        if line == 'done' :
            break
        print(line)
    print('Done!')

The **continue** statement ends the current iteration and jumps to the top of the loop and starts the next iteration

e.g.
    while True:
        line = input('> ')
        if line(0) == '#':
            continue
        if line == 'done':
            break
        print(line)
    print('Done!')

A simple **definite** loop:

for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')

