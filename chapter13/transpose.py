from PIL import Image,ImageEnhance
with Image.open("images/01.jpg") as im:
    new_im=im.transpose(Image.ROTATE_90)
    new_im.save("images/r90.jpg")
    new_im=Image.open("images/r90.jpg")
    new_im.show()
