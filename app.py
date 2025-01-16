# pake petik satu, karena direktori ada spasi
from cgitb import text
import pytesseract
from PIL import Image

alamat = r'F:\Tesseract OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = alamat
img = Image.open(r"C:\Users\Akbar\Desktop\Untitled.png")
text = pytesseract.image_to_string(img)
print(text)
