#-------------------------------------------------------------------------------
# QR-Code Generator with Docker
#-------------------------------------------------------------------------------

Note that this is an exercise that must be accomplished on your local computer!

--> Run Docker Desktop on your computer ...
--> In Visual Studio Code, open a Terminal window 
    (Menu -> Terminal -> New Terminal Window or CTRL+SHIFT+¨)

#---------------------------------------------------------------------
# Create a new folder 'QRCode_generator' in your working direktory
#---------------------------------------------------------------------

e.g. Week_03
       |--challenge
       |--exercises
         |--QRCode_generator


--> in VS Code -> Terminal cd into the folder 'QRCode_generator'

#---------------------------------------------------------------------
# Create a file 'my_script.py' with the content ...
#---------------------------------------------------------------------

from pystrich.qrcode import QRCodeEncoder

# Creates QR-Code based on text input
encoder = QRCodeEncoder("Docker ist cool!")
encoder.save( "./QRCode_test.png" )

print(encoder.get_ascii())

# Prevents the container from stopping after run
while True:
    time.sleep(1)

#---------------------------------------------------------------------
# Create a file 'Dockerfile' (no extension) with the content ...
#---------------------------------------------------------------------

FROM python:3

ADD my_script.py /

RUN pip install pystrich

CMD [ "python", "./my_script.py" ]

#-------------------------------------------------------------------
# In the Terminal window in Visual Studio Code ...
#-------------------------------------------------------------------

# Build Docker image (don't forget the point at the end of the line)
docker build -t python-qrcode .

# Run the Docker container
docker run python-qrcode

#-------------------------------------------------------------------
# Copy the QR-Code from the container to your local file system
#-------------------------------------------------------------------

--> in VS Code -> new Terminal cd into the folder 'QRCode_generator'

# Show running container and look for the container-id
docker ps

# Show running container's file system (a32950509b9e = example container-id)
docker exec -it a32950509b9e ls -l 

# Copy the .png-File to the current directory (a32950509b9e = example container-id)
docker cp a32950509b9e:QRCode_test.png QRCode_test.png

# Stop and remove the running container (a32950509b9e = example container-id)
docker stop a32950509b9e
docker rm a32950509b9e
