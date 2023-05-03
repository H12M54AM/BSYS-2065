import cImage as image

def grayscale(img):
    """Converts an image to grayscale."""
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            avg = (p.getRed() + p.getGreen() + p.getBlue()) // 3
            new_pixel = image.Pixel(avg, avg, avg)
            img.setPixel(col, row, new_pixel)

def main():
    # Load the gif image
    img = image.FileImage("./img/testimage.gif")

    # Convert the image to grayscale
    grayscale(img)

    # Save the grayscale image
    img.save("./img/testimage_gray.gif")

if __name__ == "__main__":
    main()