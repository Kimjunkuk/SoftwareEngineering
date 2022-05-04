import pygsheets
import pandas as pd
from datetime import datetime
#authorization

gc = pygsheets.authorize(service_file='C:/Users/Zinus_User/Desktop/SoftwareEngineering/RPA_projects/AutoTimeUpdater/keys.json')

# Create empty dataframe
# df = pd.DataFrame()

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('Daily Outbound Worksheet')

#select the first sheet 
wks = sh[1]

timestamp = 1625309472.357246
date_time = datetime.fromtimestamp(timestamp)
str_date_time = date_time.strftime("%d/%m/%Y %H:%M:%S")


#update the first sheet with df, starting at cell B2. 
wks.update_value('D3', str_date_time)



