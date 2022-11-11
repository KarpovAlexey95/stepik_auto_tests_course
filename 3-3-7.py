import requests
import re

fileUrl = input()

res = requests.get(fileUrl)

with open("python1.html", "wb") as f:
    f.write(res.content)

mn = set()
with open("python1.html", "r") as f:
    lines = f.read()
    lines = lines.splitlines()
    for line in lines:
        pattern = r"(<a).*href=(\"|')((\w|\d|-)*?:\/\/)?(\w(\w|\d|\.|-)*)"
        match = re.findall(pattern, line)
        for find in match:
            mn.add(find[4])
result = list(mn)
result.sort()
for link in result:
    print(link)
