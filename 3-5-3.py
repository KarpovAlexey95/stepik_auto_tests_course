import requests

api_url = "http://numbersapi.com/{}/math?json=true"

while True:
    i = input()
    if i == "exit":
        break
    res = requests.get(api_url.format(i))
    data = res.json()
    if data["found"]:
        print("Interesting")
    else:
        print("Boring")

