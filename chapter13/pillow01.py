from PIL import Image
with Image.open("images/01.jpg") as im:
    im.save("images/01_3.jpg",quality=50)