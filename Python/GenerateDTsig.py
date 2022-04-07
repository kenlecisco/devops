import hmac 
import hashlib
from socket import TCP_NODELAY
from threading import local 
import requests 
import time
import datetime
from datetime import date
import pytz

def current_milli_time():
    return round(time.time() * 1000)

#get the epoch time today and 24hr ago
current_time = current_milli_time()
one_day_ago = current_time - 86400000
current_time_str = str(current_time)
one_day_ago_str = str(one_day_ago)
print('current epoch time: ' + current_time_str)
print('one day ago epoch time:' + one_day_ago_str)

#get today date
print(datetime.datetime.now())
today = date.today() 
today = str(today)
tz_SG = pytz.timezone('Asia/Singapore')  
t = datetime.datetime.now(tz_SG)
current_clock = t.strftime("%H:%M:%S")
print(current_clock)


prToken = '8a8daa14dbd5687374d6ee19f5fe461037a7397a' 
puToken = '2d004c388773d9a370fa9ee3ac3ac9343ef14745' 
apirequest = '/modelbreaches?starttime=' + one_day_ago_str+ '&endtime=' + current_time_str 
dateID = today + " " + current_clock

sig = hmac.new(prToken.encode('ASCII'),(apirequest + '\n' + puToken+'\n'+ '20222403T065000').encode('ASCII'), hashlib.sha1).hexdigest() 

print(sig) 

print("curl -k 'https://172.19.0.251" + apirequest + "'" + " -H " + '"DTAPI-Token: ' + puToken + '"' +" -H " + '"DTAPI-Date: ' + '20220324T120000'+ '"' + " -H " + '"DTAPI-Siganture: ' + sig + '"')


