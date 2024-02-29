from pystrich.qrcode import QRCodeEncoder
import time

# Creates QR-Code based on text input
encoder = QRCodeEncoder("Docker ist cool!")
encoder.save( "./QRCode_test.png" )

print(encoder.get_ascii())

# Prevents the container from stopping
while True:
    time.sleep(1)