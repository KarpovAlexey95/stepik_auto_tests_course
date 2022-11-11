import json

startDict = dict()
classList = list()
result = dict()
jsonInput = input()
data_again = json.loads(jsonInput)

for item in data_again:
    startDict[item["name"]] = item["parents"]


for key in startDict:
        result[key] = 1


def addParents(parents):
    global startDict
    global result
    global classList
    for parent in parents:
        value = result[parent]
        if parent not in classList:
            result[parent] = value + 1
        classList.append(parent)
        addParents(startDict[parent])


for key in startDict:
    parents = startDict[key]
    addParents(parents)
    classList.clear()

keys = list(startDict.keys())
keys.sort()
for key in keys:
    print(f"{key} : {result[key]}")
