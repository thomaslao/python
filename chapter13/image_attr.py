from PIL import Image
im=Image.open("images/01.jpg")
print(im.format)
print(im.mode)
print(im.width)
print(im.height)
print(im.size)