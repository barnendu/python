import pytesseract
from PIL import Image

img= Image.open("testImage.jpg")
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
text = pytesseract.image_to_string(img , lang='eng')
print(text)
