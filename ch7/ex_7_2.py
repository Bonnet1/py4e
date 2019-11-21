# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tot = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    npos = line.find(':')
    num = line[npos+1 :]
    num = num.strip()
    num = float(num)
    tot = tot + num
    count = count + 1
conf = tot/count
print('Average spam confidence:', conf)