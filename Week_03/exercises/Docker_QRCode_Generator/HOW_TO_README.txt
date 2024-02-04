#-------------------------------------------------------------------------------
# QR-Code Generator with Docker
#-------------------------------------------------------------------------------

--> Run Docker Desktop on your computer ...
--> In Visual Studio Code, open a Terminal window 
    (Menu -> Terminal -> New Terminal Window or CTRL+SHIFT+¨)

#---------------------------------------------------------------------
# Create a new folder 'QRCode_generator' in your working direktory
#---------------------------------------------------------------------

e.g. week_03
       |--challenge
       |--exercises
         |--QRCode_generator

#---------------------------------------------------------------------
# Create a file 'my_script.py' with the content ...
#---------------------------------------------------------------------

from pystrich.qrcode import QRCodeEncoder
encoder = QRCodeEncoder("Docker ist cool!")
encoder.save( "./QRCode_test.png" )
print(encoder.get_ascii())

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

# Build the Docker image (don't forget the point at the end of the line)
docker build -t python-qrcode .

# Run the Docker container
docker run python-qrcode

#-------------------------------------------------------------------
# Copy the QR-Code from the container to your local file system
#-------------------------------------------------------------------

# Show all containers and look for the container-id
docker ps -a

# Commit the container's content into a new image named 'mysnapshot'
docker commit [container-id] mysnapshot

# Look at the images
docker images

# Run the 'mysnapshot' container and show its file system by using the Bash shell
docker run -t -i mysnapshot /bin/bash
ls

# To exit the Bash shell, type
exit

# Show the container-id of 'mysnapshot'
docker ps -a

# Copy the .png-File to the local directory (bf09fb3b64c = example container-id of 'mysnapshot')
docker cp f47c4aa4afd6:QRCode_test.png C:/Users/gell/Desktop/QRCode_test.png

(change 'C:/Users/gell/Desktop/QRCode_test.png' to your local path to save the file)


