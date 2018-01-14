import requests
import base64

img_path = "im2.jpg"
url = "http://35.161.119.73:3000/api/request"

with open(img_path, "br") as img:
    bimg = img.read()
    b64img = base64.b64encode(bimg)

r = requests.post(url, json={"image" : b64img})
