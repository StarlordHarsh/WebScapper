import requests

params = {"q": "pizza"}
r = requests.get("http://bing.com/search", params=params)
s = requests.get("http://google.com/search", params=params)
print("Status-", r.status_code)
print(r.url)
print(s.url)

