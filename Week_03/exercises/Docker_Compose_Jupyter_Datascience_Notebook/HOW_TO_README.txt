#-------------------------------------------------------------------------------
# Docker: Jupyter Datascience Notebook
#-------------------------------------------------------------------------------

--> Run Docker Desktop on your computer
--> Be sure, the Docker extension is installed in Visual Studio Code
--> In Visual Studio Code, open a new Terminal window (Upper Menu or CTRL+SHIFT+¨)

#-------------------------------------------------------------------------------
# In Visual Studio Code ...
#-------------------------------------------------------------------------------

# Go to the folder with your docker-compose.yml file, this should look like
week_03
  |--challenge
  |--exercises
    |--Docker_Compose_Jupyter_Datascience_Notebook
      |--apartments_data_kt_zuerich.ipynb
      |--apartments_data_prepared.csv
      |--HOW_TO_README.txt
      |--docker-compose.yml

# Execute the file docker-compose.yml
Right click on docker-compose.yml -> Compose up

# Alternatively, in the Terminal window, type:
docker compose up

# To show the Docker images, in the Terminal Window type:
docker images

# To show the running Docker containers, in the Terminal Window type:
docker ps

# To show the running and stopped Docker containers, in the Terminal Window type:
docker ps -a

# To access the Jupyter notebook, open the following url in a web browser
# http://127.0.0.1:8888

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