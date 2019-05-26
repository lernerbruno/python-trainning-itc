from PIL import Image
import urllib.request
import numpy as np

url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
f = urllib.request.urlretrieve(url)
image = Image.open(f)
print(image.getdata())


