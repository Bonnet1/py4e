import sqlite3
import time
import zlib

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('''
SELECT Dataset.series_id
, Dataset.year
, Dataset.period
, Dataset.value
, Series.industry_code 
, Industry.text
, Period.abbr
FROM Dataset 
LEFT JOIN Series on Dataset.series_id = Series.series_id
LEFT JOIN Industry on industry_code = Industry.code
LEFT JOIN Period on Dataset.period = Period.period
WHERE industry_code > 100000 AND Dataset.period != 'M13' AND Series.ratelevel_code = 'L'
''')

dataset = dict()
for message_row in cur :
    dataset[message_row[0],message_row[1],message_row[2],message_row[4]
    ,message_row[5],message_row[6]] = (message_row[3])

print("Loaded datapoints=",len(dataset))
# print(dataset)

inds = dict()
for (series_id, value) in list(dataset.items()):
    industry = series_id[4]
    value = value
    if industry not in inds:
        inds[industry] = value
    else:
        inds[industry] += value

# pick the top industries
topinds = sorted(inds, key=inds.get, reverse=True)
topinds = topinds[:10]
print("Top 10 Industries")
print(topinds)

counts = dict()
months = list()
years = list()
dates = list()
for (series_id, value) in list(dataset.items()):
    year = series_id[1]
    month = series_id[2]
    industry = series_id[4]
    date = str(series_id[1]) + str(series_id[2])
    value = value
    if year not in years : years.append(year)
    if month not in months : months.append(month)
    if date not in dates : dates.append(date)
    key = (date, industry)
    counts[key] = counts.get(key,0) + value

# print("Counts=", len(counts))
# print("Months=", len(months))
# print("Years=", len(years))
# print("Dates=", len(dates))

# print(counts)
# print(months)
# print(years)
# print(dates)

fhand = open('gline.js','w')
fhand.write("gline = [ ['Date'")
for topind in topinds:
    fhand.write(",'"+topind+"'")
fhand.write("]")

for date in dates:
    fhand.write(",\n['"+date+"'")
    for topind in topinds:
        key = (date, topind)
        val = counts.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]");

fhand.write("\n];\n")
fhand.close()

print("Output written to gline.js")
print("Open gline.htm to visualize the data")