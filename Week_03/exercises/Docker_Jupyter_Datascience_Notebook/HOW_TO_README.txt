#-------------------------------------------------------------------------------
# Docker: Jupyter Datascience Notebook
#-------------------------------------------------------------------------------

--> Run Docker Desktop on your computer
--> Be sure, the Docker extension is installed in Visual Studio Code
--> In Visual Studio Code, open a new Terminal window (Upper Menu or CTRL+SHIFT+¨)

#-------------------------------------------------------------------------------
# In Visual Studio Code ...
#-------------------------------------------------------------------------------

# Go to the folder with your files from Moodle, this should look like:
  week_03
    |--challenge
    |--exercises
      |--Docker_Jupyter_Datascience_Notebook
        |--apartments_data_kt_zuerich.ipynb
        |--apartments_data_prepared.csv
        |--HOW_TO_README.txt

# To show the available Docker images, in the Terminal Window type:
docker images

# To show the running Docker container, in the Terminal Window type:
docker ps

# To show the running and stopped Docker containers, in the Terminal Window type:
docker ps -a

# To pull a specific docker image from Docker Hub and run the container type:
docker run -it --rm -p 8888:8888 jupyter/datascience-notebook

# To access the container, open url in a web browser (replace 'token=...' by the token shown in your Terminal window)
http://127.0.0.1:8888/?token=...

#-------------------------------------------------------------------------------
# In the Jupyter notebook ...
#-------------------------------------------------------------------------------

# Drag and drop the two files to your Jupyter Lab environment
- apartments_data_prepared.csv
- apartments_data_kt_zuerich.ipynb

# Run the Jupyter notebook 'apartments_data_kt_zuerich.ipynb'

# To stop the Jupyter notebook server, type in your Terminal widow
CTRL+C

#-------------------------------------------------------------------------------
# In Docker Desktop ...
#-------------------------------------------------------------------------------

# Stop all running containers
# Right menu -> Containers -> check all containers -> pause button -> delete button