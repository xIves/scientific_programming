import os
import re
import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

# Function
def hydro_data():

    # Current datetime
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        # Request website with hydrodata
        url = "https://www.hydrodaten.admin.ch/de/2044.html"
        page = requests.get(url)

        # HTML-Parser
        soup = BeautifulSoup(page.content, "html.parser")

        # Find statistics about hydrological data
        table = soup.find('table', {'class': 'table-narrow'})

        # Extract data
        rows = table.find_all('td')
        html_tags = [str(i) for i in rows]

        # Compile regular expression pattern to match only numeric values
        pattern = re.compile(r'\d+')

        # Extract only numeric values from the HTML tags
        hydro_data = [float(pattern.findall(tag)[0]) for tag in html_tags]

        # Write to data frame
        df = pd.DataFrame({'datetime': dt,
                        'drain': hydro_data[0],
                        'waterlevel': hydro_data[1],
                        'temperature': hydro_data[2]},
                        index=[0])

        # Hazard level
        hl = []
        if hydro_data[0] < 500: hl = 'GS1'
        elif hydro_data[0] >= 500 and hydro_data[0] < 700: hl = 'GS2'
        elif hydro_data[0] >= 700 and hydro_data[0] < 1150: hl = 'GS3'
        elif hydro_data[0] >= 1150 and hydro_data[0] < 1400: hl = 'GS4'
        else: hl = 'GS5'

        df['hazard_level'] = hl

        # Save data to file
        # Path on Windows with filename
        filename = 'hydro_data.csv'
        # Path on Linux-Server with filename
        # filename = '/home/ubuntu/data/hydro_data.csv'

        # Check if file exists ...
        if not os.path.isfile(filename):
            # Create the file
            df.to_csv('hydro_data.csv', 
                    sep=";", 
                    encoding='utf-8',
                    index=False)
        else:
            # Append new data
            df.to_csv('hydro_data.csv', 
                    sep=";", 
                    encoding='utf-8', 
                    header=False,
                    index=False,
                    mode='a')
            
        # Show data
        # df

    except:
        pass

# Function call
hydro_data()