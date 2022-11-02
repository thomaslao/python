from PIL import Image
with Image.open("images/01.jpg") as im:
    print(im.size)
    new_im=im.resize((300,300))
    new_im.save("images/resize02.jpg")
    new_im.show()
