"""
Ch 8 Question 8 - Convert Images to greyscale
---
Edward Naidoo
BSYS-2065
May 2, 2023
"""
from PIL import Image

# open the image file
img = Image.open("./img/luther.png")

# convert the image to grayscale
gray_img = img.convert("L")

# save the grayscale image
gray_img.save("./img/gray_luther.png")