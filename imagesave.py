import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://i.pinimg.com/originals/82/4b/87/824b877bf4c731e3fcc13a8881c3e982.jpg")
print("Status", r.status_code)
img = Image.open(BytesIO(r.content))
print(img.size, img.format, img.mode)
img.save("Image1." + img.format, img.format)