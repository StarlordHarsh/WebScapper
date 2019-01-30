import requests
from bs4 import BeautifulSoup

search = input("Enter search item")
params = {"q":search}
r = requests.get("http://www.bing.com/search", params=params)
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})
print(links)

for item in links:
    print("Inside For")
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    print(item_text)
    print(item_href)