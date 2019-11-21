## Reading Files ##

Files are formatted into **flat file** to allow ingesting into python to run analysis.

Open files with the **open()** function
e.g.
handle = open(filename, mode)

The **newline** character -- represenat as **\n** in strings

A **file handle** open for read can be treated as a **sequence*** of strings where each line in the file is a string in the sequence.  Can use **for** to iterate through a sequence.

e.g.
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)

Allowing used to input and exiting with bad file names:
fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)
