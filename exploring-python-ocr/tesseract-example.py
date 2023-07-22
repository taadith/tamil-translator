from PIL import Image
import pytesseract
import numpy as np

# English text to string
print(pytesseract.image_to_string(Image.open('tesseract-sample.jpg')))

# Grabbing a list of all available languages
print(pytesseract.get_languages(config=""))

# Checking for tamil
print(pytesseract.image_to_string(Image.open('tesseract-tamil-example.png'),lang='tam'))