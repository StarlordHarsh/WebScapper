from bs4 import BeautifulSoup
import requests

search = input("Enter search term: ")
par = {"q": search}
r = requests.get("https://www.bing.com/search?q=pizza", params=par)
soup = BeautifulSoup(r.text, "html.parser")
res = soup.find("ol", {"id": "b_results"})
link = res.findAll("li", {"class": "b_algo"})

for i in link:
    it_text = i.find("a").text
    it_href = i.find("a").attrs["href"]
    print(it_href,"\n",it_text)
