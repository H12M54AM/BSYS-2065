"""
Ch 8 Question 8 - Convert Images to greyscale. Please have cImage within the same directory
---
Edward Naidoo
BSYS-2065
May 3, 2023
"""

import cImage as image

def grayscale(img):
    """
    Converts an image to grayscale.
    """
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            avg = (p.getRed() + p.getGreen() + p.getBlue()) // 3
            new_pixel = image.Pixel(avg, avg, avg)
            img.setPixel(col, row, new_pixel)

def main():
    img = image.FileImage("./img/testimage.gif")
    grayscale(img)
    img.save("./img/testimage_gray.gif")

if __name__ == "__main__":
    main()