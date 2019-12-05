import re
hand = open('regex_sum_324820.txt')
sum = 0
t = list()
count = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for numstr in x:
            numint = int(numstr)
            t.append(numint)
            count = count + numint

print(count)