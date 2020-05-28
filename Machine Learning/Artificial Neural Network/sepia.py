from PIL import Image
import os
import shutil


# convert an image to sepia
def sepia(image_path: str) -> Image:
    img = Image.open(image_path)
    width, height = img.size

    pixels = img.load()  # create the pixel map

    for py in range(height):
        for px in range(width):
            t, r, g, b = img.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255
            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            pixels[px, py] = (tr, tg, tb)

    return img


# save sepia images
def transformToSepia(fromFile, toFile):
    images = os.listdir(fromFile)
    for i in range(len(images)):
        sepia_image = sepia(fromFile + '/' + images[i])
        sepia_image.save(toFile + '/' + images[i])

# transformToSepia("20x20", "Sepia20x20")


# choose a number of sepia/non-sepia images
def chooseImages(fromOriginal, fromSepia, where):
    originalImages = os.listdir(fromOriginal)
    sepiaImages = os.listdir(fromSepia)
    for i in range(len(originalImages)):
        name = originalImages[i].split(".")[0]
        shutil.copyfile(fromOriginal + "/" + originalImages[i], where + "/" + name + "-True.png")
    for i in range(len(sepiaImages)):
        name = sepiaImages[i].split(".")[0]
        shutil.copyfile(fromSepia + "/" + sepiaImages[i], where + "/" + name + "-False.png")

# chooseImages("20x20", "Sepia20x20", "Images")




