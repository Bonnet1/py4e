name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = []
counts = dict()

for line in handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] == 'From' :
        emails.append(words[1])
    continue

for email in emails:
    if email not in counts:
        counts[email] = 1
    else:
        counts[email] += 1

max_key = None
max_val = None

for key, val in counts.items():

    if max_val is None or val > max_val:
        max_val = val
        max_key = key

print(max_key, max_val)