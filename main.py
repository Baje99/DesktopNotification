# This app will provide a way to create a customized desktop notifier application for your PC in a few simple steps using python.
# We will use request library to get information about coronavirus cases from an website and plyer library to push notification to the desktop
import datetime 
import time 
import requests 
from plyer import notification 
import json

data = None
try:
    data = requests.get("https://corona-rest-api.herokuapp.com/Api/romania")
    data = data.content.decode()
except:
    print("Fail to retrieve the data.")

if (data != None):
    dataJSON = json.loads(data)['Success']
    print(dataJSON)
    while(True):
        notification.notify(
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = dataJSON['cases'],
                        todaycases = dataJSON['todayCases'],
                        todaydeaths = dataJSON['todayDeaths'],
                        active = dataJSON["active"]),  
            app_icon = "Vexels-Office-Bulb.ico",
            timeout  = 50
        )
        time.sleep(60*60*4)