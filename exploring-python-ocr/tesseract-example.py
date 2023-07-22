from PIL import Image
import pyTesseract
import numpy as np

filename = 'tesseract-example.jpg'
img1 = np.array(Image.open(filename))
text = pyTesseract.image_to_string(img1)

print(text)