import requests

data = {"name":"Harsh","email":"@gmail.com"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data= data)
f = open("site.html", "w+")
f.write(r.text)