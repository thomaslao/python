from PIL import Image,ImageEnhance
with Image.open("images/01.jpg") as im:
    new_im=ImageEnhance.Contrast(im).enhance(0.8)
    new_im.save("images/01_contrast.jpg")