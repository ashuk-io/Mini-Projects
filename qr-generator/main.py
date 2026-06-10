import qrcode
url = input("Enter URL: ")
file = input("Enter filename to save it as : ")
if not(file.endswith('.png')):
    file = file+'.png'
qr = qrcode.make(url)
qr.save(file)   