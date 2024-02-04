#-------------------------------------------------------------------------------
# Python script to download .json - files containing charging station data 
#-------------------------------------------------------------------------------

# Libraries
from __future__ import print_function
from datetime import datetime, timedelta
import json
import urllib.request

# Function
def my_func():
    
    # Get current time
    print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    
    try:
        
        # Server request to get .json-file
        url = ('https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/'\
               'status/oicp/ch.bfe.ladestellen-elektromobilitaet.json')
        request = urllib.request.urlopen(url).read()
        data = json.loads(request)
        
        # Path on Windows with filename based on the current time
        filename = 'data-%s.json'% datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        # Path on Linux-Server with filename based on the current time
        # filename = '/home/ubuntu/data/data-%s.json'%datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                       
        # Saving the file
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
        
    except:

        pass

# Function call
my_func()


