import qrcode

im = qrcode.make("http://www.puiching.edu.mo/")
im.save("images/qr.jpg")
