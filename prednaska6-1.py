import json
import requests

if __name__ == "__main__":

    # data = {
    #     "name": "alice",
    #     "age": 30
    # }

    # json_data = json.dumps(data)

    # with open ('data.txt', 'w') as fp:
    #     fp.write(json_data)

    # with open('data.txt', 'r') as fp:
    #     x  = fp.read()

    # xdata = json.loads(x)
    # print(xdata)

    r = requests.get("http://jcu.cz/")
    if r.status_code == 200:
        print(r.content)