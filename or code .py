import qrcode

#taking UPI ID As a input
upi_id = input("Enter your UPI ID = ")

# UPI:// pay ?pa=upi_id&apn=NAME&cu=CURRENCY&TN = message

# defining the payment url based on the upi id and the payment app
#you can mpdify these urls based on the payment apps you want to support

phone_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# create qr code for each payment app 
phonepe_qr = qrcode.make(phone_url )
paytm_qr = qrcode.make(paytm_url )
google_pay_url = qrcode.make(google_pay_url )

#save the qr code to image file (optional)
phonepe_qr.save('phone_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_url.save('google_pay_qr.png')

#display the QR CODEs(you may need to install pil/pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_url.show()

