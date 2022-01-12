import qrcode
img = qrcode.make('Why would you scan a random QR code?')
type(img)
img.save("test_stuff.png")