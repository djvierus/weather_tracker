from urllib.request import urlopen
import urllib.parse, json, numpy as np, array as arr

json_file = open('appsettings.json')
json_settings = json.load(json_file)

interval=json_settings["polling_interval"]
timezone = json_settings["timezone"]
key = json_settings["key"]
aqi = json_settings["aqi"]
url = json_settings["url"]
source = json_settings["source"]
sql_host = json_settings["database_conf"]["host"]
sql_database = json_settings["database_conf"]["database"]
sql_port = json_settings["database_conf"]["port"]
sql_user = json_settings["database_conf"]["user"]
sql_pass = json_settings["database_conf"]["pass"]
city = json_settings["location"]["city"]
state =json_settings["location"]["state"]
try:
    location = np.array([city,state])
except Exception as error:
    print("An error has occurred when specifying the 'locaiton' variable:")
    print(error)