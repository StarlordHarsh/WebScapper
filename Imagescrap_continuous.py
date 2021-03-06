from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search = input("Enter the name for downloading wallpaper")
#no = int(input("Enter how many wallpapers yuo want to download"))
params = {"q": search}
r = requests.get("https://www.bing.com/images/search", params=params)
soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})

#for _ in range(1):
for item in links:
    img_obj = requests.get(item.attrs["href"])
    #print("Getting", item.attrs["href"])
    title = item.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save(""+title, img.format)
