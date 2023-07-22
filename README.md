# tamil-translator

This project aims to take a picture of a Tamil word I have taken, identify it, and then translate it for me.

07/21: My first proposed solution is using OCR and seeing if this is sufficient. It seems that with OCR, preprocessing images through grayscaling, thresholding, noise removal, and skew correction are needed to improve the accuracy. These will need to be explored at a further time.

From ChatGPT, Model GPT-4: "The Tesseract library is an open-source OCR engine developed by HP and is now maintained by Google. It supports many languages and can be trained to recognize other languages", which will be useful for identifying Tamil words. Because we already know we will only be feeding in Tamil words, we may be able to simplify the process. "Pytesseract is a Python wrapper for Tesseract."