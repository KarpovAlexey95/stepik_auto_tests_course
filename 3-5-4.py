import requests
import json

client_id = "9d50134f58171bee5017"
client_secret = "e5010bf251d59aefece2999f1bd47989"

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
result = dict()
while True:
    i = input()
    if i == 'exit':
        break
    # инициируем запрос с заголовком
    r = requests.get("https://api.artsy.net/api/artists/{}".format(i), headers=headers)
    # разбираем ответ сервера
    j = json.loads(r.text)
    if j['birthday'] not in result:
        result[j['birthday']] = list()
    result[j['birthday']].append(j['sortable_name'])

keys = list(result.keys())
keys.sort()
for key in keys:
    wtf = result[key]
    wtf.sort()
    for one in wtf:
        print(one)


