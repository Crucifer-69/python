#needs pytesseract to be installed on the system

import pytesseract
from PIL import Image

#path to pytesseract on the system(compusary)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
print("\nKeep the program and photo in the same file\n")
image = input("Enter the exact name of the image: ")
img = Image.open(image)
text1 = pytesseract.image_to_string(img)

txt = open('text.txt', 'a')

txt.write('\n\n\n'+text1 )

txt.close()

print("Operation complete")
