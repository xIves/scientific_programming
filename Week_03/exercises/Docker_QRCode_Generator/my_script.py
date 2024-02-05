from pystrich.qrcode import QRCodeEncoder

encoder = QRCodeEncoder("Docker ist cool!")
encoder.save( "./QRCode_test.png" )
print(encoder.get_ascii())