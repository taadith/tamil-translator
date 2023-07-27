# tamil-translator

This project aims to take a picture of a Tamil word I have taken, identify it, and then translate it for me.

## Log (because commit messages are often too short and gibberish):
07/26:
I am following an EasyOCR Tamil tutorial, which is perfect for what I need! I seem to be having an issue with loading the model required for Tamil and English.
...
I found my solution with the original tesseract-ocr project. I will simply run the bash commands through Python's OS library.
...
In creating a Python solution, I think a more efficient path would be a C/C++ alternative. I will consider this in the following iterations.

07/22:
I have installed the command-line version of tesseract, which succesfully works for English words, and will need to continue further exploration for pytesseract. I have installed the capability to recognize Tamil words but I have not tested this yet.
....
It seems that tesseract and it's Python wrapper pytesseract might not be an easy solution. I will do some further exploration on my own to see viable alternatives. So far, I have found EasyOCR which is an open-source tool for Python. It was built using PyTorch and supports over 80 languages, including Tamil.

07/21: 
My first proposed solution is using OCR and seeing if this is sufficient. It seems that with OCR, preprocessing images through grayscaling, thresholding, noise removal, and skew correction are needed to improve the accuracy. These will need to be explored at a further time.

From ChatGPT, Model GPT-4: "The Tesseract library is an open-source OCR engine developed by HP and is now maintained by Google. It supports many languages and can be trained to recognize other languages", which will be useful for identifying Tamil words. Because we already know we will only be feeding in Tamil words, we may be able to simplify the process. "Pytesseract is a Python wrapper for Tesseract."