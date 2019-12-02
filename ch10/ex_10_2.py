name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

times = []
counts = dict()
hours = []

for line in handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] == 'From' :
        times.append(words[5])
    continue

for time in times:
    hour, minute, second = time.split(':')
    if hour not in counts:
        counts[hour] = 1
    else :
        counts[hour] += 1

l = list()
for key, val in counts.items():
    l.append( (key, val) )

l.sort()

for key, val in l:
    print(key, val)