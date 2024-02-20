import qrcode

data = 'Fuck you'
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img=qr.make_image()
img.save('/Users/vincentcheung/Desktop/Coding/Python/Beginner-Project/qr/qr1.png')