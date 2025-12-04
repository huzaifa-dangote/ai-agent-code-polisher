import requests, json, time

def getUsers(url, active=True):
    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.text)
        users = []
        for u in data:
            if active == True:
                if "active" in u and u["active"] == True:
                    users.append(u)
            else:
                users.append(u)
        for i in range(len(users)):
            print("User:", users[i]["name"])
        return users
    else:
        print("error")
        return None


def main():
    print("starting..")
    u = getUsers("https://example.com/api/users", True)
    time.sleep(1)
    print("done!")

main()
