import cImage as image
img = image.Image("./img/testimage.gif")
col = 50
row = 50
p = img.getPixel(col, row)
newred = 255 - p.getRed()
newgreen = 255 - p.getGreen()
newblue = 255 - p.getBlue()
newpixel = image.Pixel(newred, newgreen, newblue)
img.setPixel(col, row, newpixel)