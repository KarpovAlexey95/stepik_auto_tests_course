import csv

with open("Crimes.csv") as f:
    reader = csv.reader(f)
    headers = next(reader)
    indexType = headers.index("Primary Type")
    dateIndex = headers.index("Date")
    types = dict()
    types["1"] = 2
    for row in reader:
        if (2015 == int(row[dateIndex].split()[0].split("/")[-1])):
            key = row[indexType]
            value = 0
            if key in types:
                value = types[key]
            types[key] = value + 1
maxType = str()
maximum = 0
for type in types:
    if types[type] > maximum:
        maxType = type
        maximum = types[type]

print(maxType, maximum)
