import requests, json

page = 5
counter = 0

re = requests.get("https://www.dcard.tw/_api/forums/pet/posts", params={"popular":"false"})
js = json.loads(re.text)

while counter < page:
    for post in js:
        if post["media"]:
            for img in post["media"]:
                reImg = requests.get(img["url"])
                print(img["url"])
                with open(img["url"].split("com/")[1], "wb") as f:
                    f.write(reImg.content)
    re = requests.get("https://www.dcard.tw/_api/forums/pet/posts", params={"popular":"false", "before":str(js[-1]["id"])})
    js = json.loads(re.text)
    counter += 1
