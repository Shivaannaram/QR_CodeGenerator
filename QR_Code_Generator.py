import qrcode

# QR Code Generating for paragraph information
qr=qrcode.make("This is the Example for the QR Code Generator")
qr.save("qr.png")
qr.show()


# QR Code Generation for Links:
data="https://www.google.com"
qr=qrcode.make(data)
qr.save("link.png")
qr.show()


# QR Code Generation for Our Own details
qr = qrcode.QRCode(version=5,
                   box_size=5,
                   border=2)
name=input("Enter your name: ")
age=int(input("Enter your age: "))
email=input("Enter your email: ")
mobileNo=int(input("Enter your mobileNo: "))

data={"Name":name,"Age":age,"Email":email,"MobileNo":mobileNo}
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save("details.png")
img.show()